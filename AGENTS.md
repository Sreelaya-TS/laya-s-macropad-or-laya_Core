# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

Laya Core is a 4-key OLED macropad built around the **XIAO RP2040** microcontroller. The project includes custom PCB design (KiCad), 3D-printed enclosure (Fusion 360), and firmware (KMK/CircuitPython).

## Architecture

```
laya-s-macropad-or-laya_Core/
├── Firmware/           # KMK firmware and CircuitPython code
│   ├── main.py         # Main firmware - key mappings, OLED config, macros
│   └── kmk_firmware-main/  # KMK library (CircuitPython keyboard firmware)
├── PCB/                # KiCad project files
│   ├── laya's macropad.kicad_sch   # Schematic
│   ├── laya's macropad.kicad_pcb   # PCB layout
│   └── gerber/         # Manufacturing files
├── CAD/                # Fusion 360 enclosure designs (.f3d, .step)
└── IMAGES/             # Documentation images
```

## Hardware Specifications

- **MCU**: XIAO RP2040 (RP2040-based, CircuitPython compatible)
- **OLED**: 128×64 I2C display (SSD1306) on GP4 (SDA) / GP5 (SCL)
- **Keys**: 4 MX-compatible mechanical switches

## Firmware Development

The firmware uses **KMK**, a CircuitPython-based keyboard firmware framework.

**Key files:**
- `Firmware/main.py` - Contains keymap, macros, and OLED bitmap configuration
- `Firmware/kmk_firmware-main/` - KMK library (do not modify unless extending KMK)

**To deploy firmware:**
1. Connect XIAO RP2040 via USB (appears as CIRCUITPY drive)
2. Copy `main.py` and the `kmk` folder to the CIRCUITPY drive
3. The device will auto-reload

**Current keymap (2×2 grid):**
```
[SCREENSHOT] [COPY]
[PASTE]      [UNDO]
```

**Adding new macros:** Define in `main.py` using `KC.MACRO()` with `Press`, `Release`, `Tap` from `kmk.modules.macros`.

## PCB Design (KiCad)

The PCB project is in `PCB/`. The design uses symbols and footprints from `OPL_Kicad_Library` (Seeed Studio Open Parts Library).

**To generate manufacturing files:**
1. Open `PCB/laya's macropad.kicad_pcb`
2. File → Fabrication Outputs → Gerbers
3. Export to `PCB/gerber/`

## External Library

`OPL_Kicad_Library/` contains Seeed Studio's KiCad component library (XIAO footprints, etc.). This is a separate repository/submodule.
