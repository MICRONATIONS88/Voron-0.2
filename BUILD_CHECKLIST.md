# Voron 0.2 Build Checklist

## Phase 1: Preparation

- [ ] Source all parts from BOM
- [ ] Print all parts (ABS/ASA, 40% infill, 4 walls, 5 top/bottom)
- [ ] Clean up printed parts (remove supports, check fit)
- [ ] Organize fasteners by type and size
- [ ] Read the full Voron 0.2 assembly manual

## Phase 2: Frame Assembly

- [ ] Assemble bottom frame extrusions
- [ ] Attach corner brackets and verify squareness
- [ ] Install vertical extrusions
- [ ] Attach top frame extrusions
- [ ] Verify frame squareness with calipers (diagonals should match)
- [ ] Install bottom panel

## Phase 3: Z-Axis & Bed

- [ ] Install Z motor mount
- [ ] Mount Z stepper with integrated leadscrew
- [ ] Install Z linear rail on rear extrusion
- [ ] Mount bed frame to Z carriage
- [ ] Install bed heater to aluminum plate
- [ ] Attach thermistor to bed
- [ ] Install bed springs/spacers
- [ ] Mount PEI spring steel sheet
- [ ] Test Z movement manually (smooth, no binding)

## Phase 4: A/B Motors & XY Motion

- [ ] Install A motor (left rear)
- [ ] Install B motor (right rear)
- [ ] Install X linear rail on X gantry extrusion
- [ ] Install Y linear rails on left and right extrusions
- [ ] Install idler pulleys with bearings
- [ ] Route and tension GT2 belts (A and B)
- [ ] Verify belt tension (should twang, not sag)
- [ ] Test X/Y movement manually (smooth, no binding)

## Phase 5: Toolhead (Mini Stealthburner)

- [ ] Assemble Mini Stealthburner housing
- [ ] Install extruder motor and gears
- [ ] Install hotend (Dragon/Dragonfly)
- [ ] Install heater cartridge
- [ ] Install hotend thermistor
- [ ] Mount part cooling fan (3010 blower)
- [ ] Mount hotend cooling fan (3010 axial)
- [ ] Mount toolhead on X carriage
- [ ] Verify smooth X movement with toolhead

## Phase 6: Wiring

- [ ] Mount PSU (24V)
- [ ] Mount SKR Pico controller board
- [ ] Mount Raspberry Pi
- [ ] Wire PSU to power inlet with fuse
- [ ] Wire PSU 24V to SKR Pico
- [ ] Wire 5V supply to Raspberry Pi
- [ ] Wire A/B stepper motors
- [ ] Wire Z stepper motor
- [ ] Wire extruder stepper motor
- [ ] Wire hotend heater
- [ ] Wire hotend thermistor
- [ ] Wire bed heater
- [ ] Wire bed thermistor
- [ ] Wire part cooling fan
- [ ] Wire hotend cooling fan
- [ ] Wire X endstop
- [ ] Wire Y endstop
- [ ] Wire Z endstop (or use nozzle probe)
- [ ] Cable management (zip ties, cable chain)
- [ ] Double check all connections with multimeter

## Phase 7: Electronics Setup

- [ ] Flash Klipper firmware to SKR Pico
- [ ] Install Klipper/Moonraker/Mainsail on Raspberry Pi
- [ ] Connect Raspberry Pi to SKR Pico via USB
- [ ] Upload printer.cfg and macros.cfg
- [ ] Verify MCU connection (`ls /dev/serial/by-id/`)

## Phase 8: Initial Configuration

- [ ] Verify all endstops (`QUERY_ENDSTOPS`)
- [ ] Verify stepper motor directions (each axis moves correctly)
- [ ] Verify heater operation (hotend heats up)
- [ ] Verify bed heater operation
- [ ] Verify fan operation (part fan, hotend fan)
- [ ] Verify thermistor readings are reasonable

## Phase 9: Calibration

- [ ] PID tune hotend (`PID_CALIBRATE HEATER=extruder TARGET=245`)
- [ ] PID tune bed (`PID_CALIBRATE HEATER=heater_bed TARGET=100`)
- [ ] Home all axes and verify correct positions
- [ ] Calibrate Z offset (paper test or probe)
- [ ] Level bed with `BED_SCREWS_ADJUST`
- [ ] Calibrate extruder rotation_distance (e-steps)
- [ ] Calibrate pressure advance per filament
- [ ] Print test cube and verify dimensions
- [ ] Input shaper calibration (optional, with ADXL345)

## Phase 10: First Print

- [ ] Slice a test model (Voron cube recommended)
- [ ] Configure slicer start/end G-code to use PRINT_START/PRINT_END
- [ ] Print first layer test
- [ ] Adjust Z offset if needed
- [ ] Print full test cube
- [ ] Verify dimensional accuracy
- [ ] Celebrate!

## Phase 11: Enclosure (Optional)

- [ ] Install side panels
- [ ] Install front panel with hinges/magnets
- [ ] Install top panel
- [ ] Install skirts
- [ ] Install tophat for extra Z height (optional)
- [ ] Install LED lighting (optional)
- [ ] Install camera for remote monitoring (optional)
