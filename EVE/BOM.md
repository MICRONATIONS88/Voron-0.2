# EVE - Bill of Materials

## Frame & Enclosure

| Qty | Part | Spec | Sourced |
|-----|------|------|---------|
| 8 | Extrusion | Makerbeam XL 15x15mm (various lengths) | [ ] |
| 1 | Top Panel | 3mm Acrylic / Polycarbonate | [ ] |
| 2 | Side Panels | 3mm Acrylic / Polycarbonate | [ ] |
| 1 | Front Panel | 3mm Acrylic / Polycarbonate | [ ] |
| 1 | Back Panel | 3mm Acrylic / Polycarbonate | [ ] |
| 1 | Bottom Panel | 3mm ACM / Aluminum | [ ] |

## Motion

| Qty | Part | Spec | Sourced |
|-----|------|------|---------|
| 5 | Linear Rail | MGN7H 150mm | [ ] |
| 2 | Stepper Motor (A/B) | NEMA14 (LDO-35STH52-1504AH) | [ ] |
| 1 | Stepper Motor (Z) | NEMA17 integrated leadscrew (LDO-42STH25-1004CL200E) | [ ] |
| 1 | Stepper Motor (Extruder) | NEMA14 36mm pancake (LDO-36STH20-1004AHG) | [ ] |
| 2 | GT2 Belt | 6mm, ~600mm | [ ] |
| 6 | F623-RS Bearing | Flanged bearing for idlers | [ ] |
| 2 | GT2 20T Pulley | 5mm bore, 6mm belt width | [ ] |

## Electronics

| Qty | Part | Spec | Sourced |
|-----|------|------|---------|
| 1 | MCU | BTT SKR Pico v1.0 | [ ] |
| 1 | SBC | **BTT Pi v1.2** | [ ] |
| 1 | PSU | Mean Well LRS-150-24 (24V 150W) | [ ] |
| 1 | 5V Supply | DC-DC Buck converter (or BTT Pi powered via USB) | [ ] |
| 1 | Power Inlet | IEC320 C14 with fuse and switch | [ ] |
| 1 | MicroSD Card | 16GB+ for BTT Pi | [ ] |

### BTT Pi v1.2 Details

- Allwinner H616 quad-core CPU
- 1GB DDR3L RAM
- Onboard WiFi + Ethernet
- Compatible with CB1 images (Armbian / BTT CB1 OS)
- GPIO header compatible with Raspberry Pi HATs
- USB-C power input (5V/3A)

## Toolhead: Dragonburner

| Qty | Part | Spec | Sourced |
|-----|------|------|---------|
| 1 | Hotend | **Bambu Lab hotend** (bi-metal heatbreak, quick-swap nozzle) | [ ] |
| 1 | Heater Cartridge | 48W 24V (Bambu Lab ceramic heater) | [ ] |
| 1 | Thermistor | NTC 100K (Bambu Lab stock, Generic 3950 compatible) | [ ] |
| 1 | Nozzle | Bambu Lab 0.4mm hardened steel / brass | [ ] |
| 2 | Part Cooling Fan | **4010 Blower 24V** (dual fans) | [ ] |
| 1 | Hotend Fan | **2510 Axial 24V** | [ ] |
| 1 | Bowden Tube | PTFE 4x2mm (short section for extruder) | [ ] |
| 1 | Extruder | CW2 / Galileo 2 / Sherpa Mini | [ ] |

## Bed

| Qty | Part | Spec | Sourced |
|-----|------|------|---------|
| 1 | Build Plate | 120x120mm Aluminum tooling plate | [ ] |
| 1 | Bed Heater | 60W 24V silicone heater | [ ] |
| 1 | PEI Sheet | 120x120mm spring steel + PEI (textured) | [ ] |
| 3 | Bed Spacer | M3x10mm standoff | [ ] |
| 3 | Bed Spring | Silicone spacer | [ ] |

## Fasteners

| Qty | Part | Spec | Sourced |
|-----|------|------|---------|
| ~50 | M2x6 SHCS | Socket head cap screw | [ ] |
| ~40 | M3x6 SHCS | Socket head cap screw | [ ] |
| ~30 | M3x8 SHCS | Socket head cap screw | [ ] |
| ~20 | M3x12 SHCS | Socket head cap screw | [ ] |
| ~10 | M3x16 SHCS | Socket head cap screw | [ ] |
| ~20 | M3 T-nut | Roll-in or slide-in | [ ] |
| ~20 | M3 Hex Nut | Standard | [ ] |
| ~15 | M3 Heatset Insert | M3x5x4mm brass | [ ] |
| ~10 | M2 Heatset Insert | M2x3.5x4mm brass | [ ] |

## Wiring & Misc

| Qty | Part | Spec | Sourced |
|-----|------|------|---------|
| 1m | Silicone Wire 20AWG | Heater, PSU | [ ] |
| 3m | Silicone Wire 24AWG | Signals, fans | [ ] |
| 1 | Microswitch | X endstop | [ ] |
| 1 | Microswitch | Y endstop | [ ] |
| - | Wire Connectors | JST-XH, Microfit3 | [ ] |
| - | Zip Ties | 100mm | [ ] |
| 1 | USB-C Cable | BTT Pi to SKR Pico | [ ] |

## Printed Parts

All parts: ABS/ASA, 40% infill, 4 perimeters.

- Frame components (standard V0.2)
- **Dragonburner toolhead** (different from standard Mini Stealthburner)
- X carriage (Dragonburner specific)
- AB motor mounts
- Z motor mount
- Bed frame
- Skirts

Dragonburner STLs: https://github.com/chirpy2605/voron/tree/main/V0/Dragon_Burner
