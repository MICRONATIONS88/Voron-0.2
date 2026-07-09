import os
import sys
import time
import shutil

VARIABLES_FILE = '/home/adam/printer_data/config/variables.cfg'
GCODES_DIR     = '/home/adam/printer_data/gcodes'
OUTPUT_NAME    = 'plr_resume.gcode'
OUTPUT_FILE    = os.path.join(GCODES_DIR, OUTPUT_NAME)

def parse_variables(path):
    variables = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if '=' in line and not line.startswith('['):
                    key, _, val = line.partition('=')
                    variables[key.strip()] = val.strip().strip("'\"")
    except Exception as e:
        print(f"ERROR reading variables: {e}")
        sys.exit(1)
    return variables

def find_gcode(gcodes_dir, filename):
    direct = os.path.join(gcodes_dir, filename)
    if os.path.exists(direct):
        return direct
    for root, _, files in os.walk(gcodes_dir):
        if os.path.basename(filename) in files:
            return os.path.join(root, os.path.basename(filename))
    return None

def process_gcode_ultra_fast(gcode_path, target_z):
    last_fan = None
    last_feedrate = None
    split_line_idx = None
    prev_z = 0.0
    last_layer_comment_idx = None
    
    with open(gcode_path, 'r', errors='replace') as f:
        for i, line in enumerate(f):
            s = line.strip()
            if not s:
                continue
            
            if s.startswith(';'):
                if 'LAYER' in s.upper():
                    su = s.upper()
                    if any(tok in su for tok in [';LAYER_CHANGE', ';AFTER_LAYER_CHANGE', ';LAYER:', '; LAYER ']):
                        last_layer_comment_idx = i
                continue
                
            # Fan speed
            if s.startswith('M106') or s.startswith('m106'):
                last_fan = s
                continue
            
            # Moves (G0/G1/G2/G3 etc)
            if s.startswith('G') or s.startswith('g'):
                parts = s.split()
                if not parts:
                    continue
                cmd = parts[0].upper()
                if cmd in ('G0', 'G1', 'G2', 'G3', 'G92'):
                    has_z = False
                    for p in parts[1:]:
                        pu = p.upper()
                        if pu.startswith('F'):
                            last_feedrate = pu[1:]
                        elif pu.startswith('Z'):
                            has_z = True
                            try:
                                z = float(pu[1:])
                                if z >= target_z and prev_z < target_z:
                                    split_line_idx = i
                                    if last_layer_comment_idx is not None and (i - last_layer_comment_idx < 40):
                                        split_line_idx = last_layer_comment_idx
                                    break
                                if z > 0:
                                    prev_z = z
                            except ValueError:
                                pass
                    if split_line_idx is not None:
                        break
                            
    return split_line_idx, last_fan, last_feedrate

def main():
    t0 = time.time()
    variables = parse_variables(VARIABLES_FILE)

    filename = variables.get('resume_filename', '').strip("'\"")
    if not filename:
        print("ERROR: resume_filename not saved in variables.cfg.")
        sys.exit(1)

    try:
        resume_z = float(variables.get('resume_z', 0))
    except ValueError:
        resume_z = 0.0
    if resume_z <= 0:
        print(f"ERROR: Invalid resume_z ({resume_z})")
        sys.exit(1)

    gcode_path = find_gcode(GCODES_DIR, filename)
    if not gcode_path:
        print(f"ERROR: Gcode file not found: {filename}")
        sys.exit(1)

    print(f"Source : {gcode_path}")
    print(f"Resume Z: {resume_z} mm")

    split_index, last_fan, last_feedrate = process_gcode_ultra_fast(gcode_path, resume_z)

    if split_index is None:
        print(f"ERROR: Could not locate Z={resume_z} in the gcode file.")
        sys.exit(1)

    print(f"Split at line {split_index + 1}  (fan={last_fan}, feedrate={last_feedrate})")

    header = [
        f'; === PLR Resume - auto-generated ===\n',
        f'; Source  : {os.path.basename(gcode_path)}\n',
        f'; Resume Z: {resume_z} mm  (split at line {split_index + 1})\n',
        ';\n',
        'G90       ; absolute positioning\n',
        'M82       ; absolute extrusion\n',
        'G92 E0    ; reset extruder\n',
    ]
    if last_fan:
        header.append(f'{last_fan}  ; restore fan\n')
    if last_feedrate:
        header.append(f'G1 F{last_feedrate}  ; restore feedrate\n')
    header.append(';\n')

    # Copy the remaining lines to OUTPUT_FILE
    with open(OUTPUT_FILE, 'w') as out_f:
        out_f.writelines(header)
        with open(gcode_path, 'r', errors='replace') as in_f:
            for idx, line in enumerate(in_f):
                if idx >= split_index:
                    out_f.write(line)
                    shutil.copyfileobj(in_f, out_f)
                    break

    t1 = time.time()
    print(f"SUCCESS: Written to {OUTPUT_FILE} (elapsed: {t1 - t0:.4f}s)")

if __name__ == '__main__':
    main()
