# =================================================
# KMK Coding Macropad
# Board: Seeed Studio XIAO RP2040
# File: code.py
# =================================================

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

# -------------------------------------------------
# Keyboard instance
# -------------------------------------------------
keyboard = KMKKeyboard()

# -------------------------------------------------
# Enable macros
# -------------------------------------------------
macros = Macros()
keyboard.modules.append(macros)

# -------------------------------------------------
# Button pins (change if your wiring differs)
# -------------------------------------------------
PINS = [
    board.D1,   # Key 1
    board.D2,   # Key 2
    board.D3,   # Key 3
    board.D4,   # Key 4
]

# -------------------------------------------------
# Individual buttons (no matrix)
# -------------------------------------------------
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# -------------------------------------------------
# Keymap (Coding shortcuts)
# -------------------------------------------------
keyboard.keymap = [
    [
        # SAVE  (Ctrl + S)
        KC.Macro(
            Press(KC.LCTRL),
            Tap(KC.S),
            Release(KC.LCTRL),
        ),

        # COPY  (Ctrl + C)
        KC.Macro(
            Press(KC.LCTRL),
            Tap(KC.C),
            Release(KC.LCTRL),
        ),

        # PASTE (Ctrl + V)
        KC.Macro(
            Press(KC.LCTRL),
            Tap(KC.V),
            Release(KC.LCTRL),
        ),

        # UNDO  (Ctrl + Z)
        KC.Macro(
            Press(KC.LCTRL),
            Tap(KC.Z),
            Release(KC.LCTRL),
        ),
    ]
]

# -------------------------------------------------
# Start KMK
# -------------------------------------------------
if __name__ == "__main__":
    keyboard.go()
