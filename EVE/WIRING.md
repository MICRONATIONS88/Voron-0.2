# EVE - Wiring Reference

## BTT SKR Pico v1.0 Pinout

### Stepper Motors

| Motor | Function | Step | Dir | Enable | UART Addr |
|-------|----------|------|-----|--------|-----------|
| M1 | Stepper X (B Motor) | gpio11 | gpio10 | gpio12 | 0 |
| M2 | Stepper Y (A Motor) | gpio6 | gpio5 | gpio7 | 2 |
| M3 | Stepper Z | gpio19 | gpio28 | gpio2 | 1 |
| M4 | Extruder | gpio14 | gpio13 | gpio15 | 3 |

UART Bus: TX=gpio8, RX=gpio9 (shared bus, addressed by uart_address)

### Endstops

| Endstop | Pin | Location |
|---------|-----|----------|
| X | gpio4 | X max |
| Y | gpio3 | Y max |
| Z | gpio25 | Z endstop |

### Heaters

| Heater | Pin | Sensor Pin | Sensor Type |
|--------|-----|------------|-------------|
| Hotend (HE0) | gpio23 | gpio27 | Generic 3950 (Bambu Lab NTC 100K) |
| Bed (HB) | gpio21 | gpio26 | Generic 3950 |

### Fans (Dragonburner Configuration)

| Fan | Pin | Type | Notes |
|-----|-----|------|-------|
| Part Cooling (FAN0) | gpio17 | PWM | 2x 4010 blower in parallel |
| Hotend Fan (FAN1) | gpio18 | Auto on >50C | 1x 2510 axial |

**Dragonburner Fan Wiring:**
```
FAN0 (gpio17) ──┬── 4010 Blower Left  (+/-)
                 └── 4010 Blower Right (+/-)

FAN1 (gpio18) ──── 2510 Axial Hotend Fan (+/-)
```

Both 4010 blowers are wired in parallel to the same FAN0 output.
Ensure total current draw does not exceed the MOSFET rating (~1A).

### NeoPixel LEDs (Matchstick)

| LED | Pin | Count | Notes |
|-----|-----|-------|-------|
| NeoPixel (RGB header) | gpio24 | 20 | WS2812, GRB color order |

**Wiring:**
```
SKR Pico RGB (gpio24) → Left Matchstick (10 LEDs) → Right Matchstick (10 LEDs)
                         LED 1-10                     LED 11-20
```
- データラインをデイジーチェーン接続（Left OUT → Right IN）
- 5V/GND は SKR Pico の RGB ヘッダーから供給

## BTT Pi v1.2 Connections

| Connection | Method | Notes |
|------------|--------|-------|
| SKR Pico | USB-C cable | Klipper MCU communication |
| Network | WiFi or Ethernet | Mainsail/Fluidd web interface |
| Power | USB-C 5V/3A | From 5V buck converter or USB PSU |
| ADXL345 (opt) | SPI via GPIO | Input shaper calibration |

### BTT Pi Setup Notes

1. Flash CB1 OS image (or Armbian) to MicroSD
2. Install Klipper + Moonraker + Mainsail via KIAUH
3. Configure WiFi in `/boot/system.cfg` before first boot
4. SSH default: `biqu` / `biqu`

## Power Distribution

```
AC Inlet (w/ fuse & switch)
  |
  +-- Mean Well LRS-150-24
        |
        +-- 24V --> SKR Pico VIN
        |     +-- Hotend heater (via HE0 MOSFET)
        |     +-- Bed heater (via HB MOSFET)
        |     +-- 2x 4010 blower fans (via FAN0)
        |     +-- 2510 hotend fan (via FAN1)
        |     +-- Stepper motors (A, B, Z, E)
        |     +-- NeoPixel matchstick LEDs (via RGB header)
        |
        +-- DC-DC Buck 24V -> 5V
              |
              +-- BTT Pi (USB-C 5V/3A)
```

## Important Notes

1. **BTT Pi Power**: Use a quality 5V/3A supply. Undervoltage causes
   random crashes. Do NOT power from SKR Pico 5V pin.

2. **Dual Fan Wiring**: Both 4010 blowers share one output. Match
   polarity carefully. Total draw ~0.3A typical.

3. **Dragonburner Fan Clearance**: Route fan wires through the toolhead
   cable path. Keep clear of hotend heatsink.

4. **Wire Gauge**:
   - 20 AWG: Heaters, PSU connections
   - 24 AWG: Stepper motors, fans
   - 26-28 AWG: Thermistors, endstops

5. **USB Cable**: Use a short, quality USB-C cable between BTT Pi and
   SKR Pico to avoid communication issues.
