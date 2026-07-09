import os
import re
import sys
import time
import shutil

VARIABLES_FILE = '/dev/shm/variables.cfg'
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

def process_gcode_fast(gcode_path, target_z):
    last_fan = None
    last_feedrate = None
    split_line_idx = None
    prev_z = 0.0
    
    recent_lines = []
    
    with open(gcode_path, 'r', errors='replace') as f:
        for i, line in enumerate(f):
            s = line.strip()
            if not s:
                continue
            
            recent_lines.append((i, line))
            if len(recent_lines) > 16:
                recent_lines.pop(0)
                
            su = s.upper()
            
            # Fan speed
            if su.startswith('M106'):
                last_fan = s
                
            # Feedrate in G0/G1
            if su.startswith('G0 ') or su.startswith('G1 '):
                idx = su.find('F')
                if idx != -1 and (idx == 0 or su[idx-1].isspace()):
                    digits = []
                    for char in su[idx+1:]:
                        if char.isdigit() or char == '.':
                            digits.append(char)
                        else:
                            break
                    if digits:
                        last_feedrate = "".join(digits)
            
            # Z height check
            if not s.startswith(';'):
                idx = su.find('Z')
                if idx != -1 and (idx == 0 or su[idx-1].isspace()):
                    digits = []
                    for char in su[idx+1:]:
                        if char.isdigit() or char == '.' or char == '-':
                            digits.append(char)
                        else:
                            break
                    if digits:
                        try:
                            z = float("".join(digits))
                            if z >= target_z and prev_z < target_z:
                                split_line_idx = i
                                for ri, rline in recent_lines[:-1]:
                                    ru = rline.strip().upper()
                                    if any(tok in ru for tok in [';LAYER_CHANGE', ';AFTER_LAYER_CHANGE', ';LAYER:', '; LAYER ']):
                                        split_line_idx = ri
                                        break
                                break
                            if z > 0:
                                prev_z = z
                        except ValueError:
                            pass
                            
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

    split_index, last_fan, last_feedrate = process_gcode_fast(gcode_path, resume_z)

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
    header.append(';\n')

    # Copy the remaining lines to OUTPUT_FILE
    with open(OUTPUT_FILE, 'w') as out_f:
        out_f.writelines(header)
        with open(gcode_path, 'r', errors='replace') as in_f:
            for idx, line in enumerate(in_f):
                if idx >= split_index:
                    out_f.write(line)
                    # We can write in chunks or line by line. Line-by-line is fine,
                    # but we can write the rest in blocks for maximum efficiency.
                    shutil.copyfileobj(in_f, out_f)
                    break

    t1 = time.time()
    print(f"SUCCESS: Written to {OUTPUT_FILE} (elapsed: {t1 - t0:.4f}s)")

if __name__ == '__main__':
    main()
