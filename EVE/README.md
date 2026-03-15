# EVE - Voron 0.2 Build #2

## Specs

| Item | Value |
|------|-------|
| Name | EVE |
| Build Volume | 120 x 120 x 120 mm |
| Motion System | CoreXY |
| Firmware | Klipper |
| Toolhead | Dragonburner |
| Hotend | Bambu Lab hotend (bi-metal) |
| Bed | 120mm Aluminum with DC heater |
| MCU | BTT SKR Pico v1.0 |
| SBC | BTT Pi v1.2 |
| Kinematics | CoreXY with MGN7H linear rails |

## Dragonburner Toolhead

Dragonburner is a high-performance toolhead for Voron 0 with:
- Dual 4010 blower fans for part cooling
- 2510 axial fan for hotend cooling
- Improved cooling duct geometry
- Compatible with Dragon, Rapido, Bambu Lab, and other hotends
- CW2 / Galileo 2 extruder compatible

STL source: https://github.com/chirpy2605/voron/tree/main/V0/Dragon_Burner

## Key Differences from Build #1

| Feature | Build #1 | EVE (Build #2) |
|---------|----------|-----------------|
| SBC | Raspberry Pi | BTT Pi v1.2 |
| Toolhead | Mini Stealthburner | Dragonburner |
| Hotend | Dragon / Dragonfly | Bambu Lab (bi-metal) |
| Part Fan | 1x 3010 blower | 2x 4010 blower |
| Hotend Fan | 3010 axial | 2510 axial |
| Cooling | Standard | Enhanced |

## BTT Pi Environment

| Item | Value |
|------|-------|
| User | biqu |
| Hostname | bigtreetech-cb1 |
| OS | Armbian (CB1) |
| MCU Serial | `usb-Klipper_rp2040_504434040883CA1C-if00` |
| Config Tool | armbian-config |
| Monitoring | htop |
| Local IP | 192.168.0.x |

## File Structure

```
EVE/
  README.md          # This file
  BOM.md             # Bill of Materials
  WIRING.md          # Wiring reference
  firmware/
    printer.cfg      # Klipper main config
    macros.cfg       # Custom G-code macros
  docs/              # Additional docs
  images/            # Build photos
```
