# Voron 0.2 Build Project

Voron 0.2 CoreXY 3D printer builds.

## Builds

| # | Name | SBC | MCU | Toolhead | Status |
|---|------|-----|-----|----------|--------|
| 1 | (Build 1) | Raspberry Pi | SKR Pico | Mini Stealthburner | Planning |
| 2 | **EVE** | BTT Pi v1.2 | SKR Pico | Dragonburner | Planning |

## Common Specs

| Item | Value |
|------|-------|
| Build Volume | 120 x 120 x 120 mm |
| Motion System | CoreXY |
| Firmware | Klipper |
| Kinematics | CoreXY with MGN7H linear rails |

## Project Structure

```
Voron-0.2/
  BOM.md                # Build 1 - Bill of Materials
  BUILD_CHECKLIST.md     # Build 1 - Build tracking
  WIRING.md              # Build 1 - Wiring reference
  firmware/              # Build 1 - Klipper config
    printer.cfg
    macros.cfg
  EVE/                   # Build 2 - EVE
    README.md            # EVE specs & details
    BOM.md               # EVE Bill of Materials
    WIRING.md            # EVE Wiring reference
    firmware/
      printer.cfg        # EVE Klipper config
      macros.cfg         # EVE macros
```

## Resources

- Voron Design: https://vorondesign.com/voron0.2
- Voron GitHub: https://github.com/VoronDesign/Voron-0
- Dragonburner: https://github.com/chirpy2605/voron/tree/main/V0/Dragon_Burner
- Klipper Docs: https://www.klipper3d.org/
- Voron Discord: https://discord.gg/voron
