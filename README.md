# Voron 0.2 Build Project

Voron 0.2 CoreXY 3D printer build project.

## Specs

| Item | Value |
|------|-------|
| Build Volume | 120 x 120 x 120 mm |
| Motion System | CoreXY |
| Firmware | Klipper |
| Extruder | Mini Stealthburner (Direct Drive) |
| Hotend | Dragon / Dragonfly |
| Bed | 120mm Aluminum with AC or DC heater |
| Controller | SKR Pico / Raspberry Pi |
| Kinematics | CoreXY with MGN7H linear rails |

## Project Structure

```
Voron-0.2/
  BOM.md              # Bill of Materials with sourcing info
  BUILD_CHECKLIST.md   # Step-by-step build tracking
  WIRING.md            # Wiring reference and pinout
  firmware/
    printer.cfg        # Klipper main configuration
    macros.cfg         # Custom G-code macros
  docs/                # Additional documentation
  images/              # Build photos
```

## Resources

- Voron Design: https://vorondesign.com/voron0.2
- Voron GitHub: https://github.com/VoronDesign/Voron-0
- Klipper Docs: https://www.klipper3d.org/
- Voron Discord: https://discord.gg/voron
