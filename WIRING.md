# Voron 0.2 Wiring Reference

## BTT SKR Pico v1.0 Pinout

### Stepper Motors

| Motor | Function | Step | Dir | Enable | UART |
|-------|----------|------|-----|--------|------|
| M1 | Stepper X (B Motor) | gpio11 | gpio10 | gpio12 | uart0 |
| M2 | Stepper Y (A Motor) | gpio6 | gpio5 | gpio7 | uart2 |
| M3 | Stepper Z | gpio19 | gpio28 | gpio2 | uart1 |
| M4 | Extruder | gpio14 | gpio13 | gpio15 | uart3 |

UART Bus: TX=gpio8, RX=gpio9 (shared, addressed by uart_address)

### Endstops

| Endstop | Pin | Location |
|---------|-----|----------|
| X | gpio4 | X-axis max position |
| Y | gpio3 | Y-axis max position |
| Z | gpio25 | Z-axis (nozzle or switch) |

### Heaters

| Heater | Pin | Sensor Pin | Sensor Type |
|--------|-----|------------|-------------|
| Hotend (HE0) | gpio23 | gpio27 | ATC Semitec 104NT-4 |
| Bed (HB) | gpio21 | gpio26 | Generic 3950 |

### Fans

| Fan | Pin | Type |
|-----|-----|------|
| Part Cooling (FAN0) | gpio17 | PWM controllable |
| Hotend Fan (FAN1) | gpio18 | Always on above 50C |

### Other Connections

| Connection | Pin | Notes |
|------------|-----|-------|
| Neopixel | gpio24 | Optional LED strip |
| Servo | gpio29 | Optional (Klicky probe) |

## Wiring Color Convention

| Color | Signal |
|-------|--------|
| Red | 24V / VCC |
| Black | GND |
| Green | Step / Signal A |
| Blue | Dir / Signal B |
| Yellow | Enable / Signal |
| White | Thermistor / Signal |

## Power Distribution

```
AC Inlet (w/ fuse & switch)
  |
  +-- Mean Well LRS-150-24
  |     |
  |     +-- 24V --> SKR Pico (VIN)
  |     +-- 24V --> Bed Heater
  |     +-- 24V --> Hotend Heater (via MOSFET on board)
  |     +-- 24V --> Fans (via MOSFET on board)
  |
  +-- 5V Supply (buck converter or separate PSU)
        |
        +-- 5V --> Raspberry Pi (GPIO header or USB-C)
```

## Important Notes

1. **Stepper Direction**: If a motor moves the wrong way, add or remove `!`
   before the `dir_pin` in printer.cfg (e.g., `dir_pin: !gpio10`)

2. **Endstop Logic**: The `^` prefix enables internal pullup. Use `^!` for
   inverted logic (NC switches).

3. **Thermistor Wiring**: Keep thermistor wires away from stepper/heater wires
   to avoid noise. Use twisted pair if possible.

4. **Ground**: Ensure all grounds (24V PSU, 5V PSU, SKR Pico, Pi) share a
   common ground reference.

5. **Wire Gauge**:
   - 20 AWG: Heaters, PSU connections
   - 24 AWG: Stepper motors, fans, signals
   - 26-28 AWG: Thermistors, endstops

6. **Crimping**: Use proper JST-XH and Microfit 3.0 connectors. Avoid
   soldering directly to the board.
