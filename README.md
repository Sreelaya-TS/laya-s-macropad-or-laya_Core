# Laya Core – 4-Key OLED Macropad ⌨️🤖

**Laya Core** is a compact **4-key custom macropad** built using the **XIAO RP2040**, powered by **KMK firmware**, and enhanced with an **OLED display** for visual feedback.  
It is designed for productivity shortcuts like screenshots, copy-paste, window control, and custom macros.

This project includes a **custom PCB**, **KMK firmware**, and a **3D-printed case**, making it a complete end-to-end hardware build.

---

## ✨ Features

- 4 programmable mechanical keys  
- XIAO RP2040 microcontroller  
- OLED display (I2C, 128×64)  
- KMK (CircuitPython-based) firmware  
- Custom PCB designed in KiCad  
- 3D printed enclosure (Fusion 360)  
- Compact, beginner-friendly design  

---

## 🧠 Firmware

- Written using **KMK firmware**
- Supports:
  - Custom keyboard shortcuts (screenshots, copy, paste, etc.)
  - Layer-based key mapping
  - Macro support
  - OLED bitmap display (cute robot graphic)

> Firmware source code is available in this repository.

---

## 📸 Project Images

### 🟢 PCB Layout
<!-- Add your PCB image here -->
![PCB Layout](IMAGES/pcb.png)

---

### 🔵 Schematic
<!-- Add your schematic image here -->
![Schematic](IMAGES/schematic.png)

---

### 🟣 Final 3D Model (Fusion 360)
<!-- Add your Fusion 360 render here -->
![Final 3D Model](IMAGES/final_fusion.png)

---

## 🔌 OLED Display

- OLED communicates via **I2C**
- Resolution: **128 × 64**
- Driver: **SSD1306**
- Displays a custom bitmap (robot illustration)

### Display behavior
- Currently configured as **always-on**
- Can be upgraded to:
  - Key-triggered display
  - Layer indicator
  - Simple animations

---

## 🧩 Bill of Materials (BOM)

> 💡 Prices are approximate and may vary depending on supplier.

| Sl No | Component                              | Quantity | Approx Price (₹) | Total (₹) |
|-----:|---------------------------------------|---------:|-----------------:|----------:|
| 1    | XIAO RP2040 Microcontroller           | 1 | 650 | 650 |
| 2    | Mechanical Switches (MX compatible)   | 4 | 50 | 200 |
| 3    | Keycaps                               | 4 | 40 | 160 |
| 4    | OLED Display (SSD1306, 128×64, I2C)   | 1 | 250 | 250 |
| 5    | Diodes (1N4148 / SMD)                 | 4 | 5 | 20 |
| 6    | Custom PCB                            | 1 | 300 | 300 |
| 7    | Reset Button (SMD / Through-hole)     | 1 | 20 | 20 |
| 8    | USB Type-C Cable                      | 1 | 100 | 100 |
| 9    | 3D Printed Case                      | 1 | 250 | 250 |
| 10   | Screws / Spacers                     | As required | 50 | 50 |

### 💰 **Estimated Total Cost:** **₹2,020**

---

## 🛠️ Tools Used

- **KiCad** – schematic and PCB design  
- **Fusion 360** – 3D modeling  
- **KMK Firmware** – keyboard firmware  
- **CircuitPython**  
- **Git & GitHub**

---

## 🚀 Future Improvements

- OLED animations
- Multiple layers with visual indicators
- RGB underglow
- Rotary encoder support
- Configurable display modes

---

## 💙 Author

**Sreelaya TS**  
Electronics • Embedded Systems • Custom Keyboards  

---

⭐ If you like this project, consider starring the repository!
