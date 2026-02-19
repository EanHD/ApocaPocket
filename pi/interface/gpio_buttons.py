#!/usr/bin/env python3
"""
GPIO button handler for Pi Zero 2 W physical interface.
Maps physical buttons to keyboard events for the TUI.

Wiring (BCM pin numbers — updated for Waveshare 2" SPI display build):
  - UP:     GPIO 5  (pin 29)
  - DOWN:   GPIO 6  (pin 31)
  - SELECT: GPIO 16 (pin 36)
  - BACK:   GPIO 26 (pin 37)
  - POWER:  GPIO 21 (pin 40)  [long-press = shutdown]

All buttons: connect between GPIO pin and GND, using internal pull-ups.
"""

import subprocess
import sys
import time
import os

try:
    from gpiozero import Button
    from signal import pause
    HAS_GPIO = True
except ImportError:
    HAS_GPIO = False
    print("gpiozero not available — GPIO buttons disabled (keyboard-only mode)")


# Button-to-key mapping using uinput or direct stdin injection
# We'll use a simpler approach: write to a named pipe that the TUI reads

FIFO_PATH = "/tmp/fieldnode_buttons"
SHUTDOWN_HOLD_SEC = 3


def send_key(key_name):
    """Write key event to FIFO for TUI consumption."""
    try:
        with open(FIFO_PATH, "w") as f:
            f.write(key_name + "\n")
    except Exception:
        pass


def on_up():
    send_key("UP")

def on_down():
    send_key("DOWN")

def on_select():
    send_key("SELECT")

def on_back():
    send_key("BACK")


class PowerButton:
    def __init__(self, pin=24):
        self.btn = Button(pin, hold_time=SHUTDOWN_HOLD_SEC)
        self.btn.when_held = self._shutdown

    def _shutdown(self):
        print("Power button held — shutting down...")
        subprocess.run(["sudo", "shutdown", "-h", "now"])


def main():
    if not HAS_GPIO:
        print("No GPIO available. Use keyboard with the TUI directly.")
        sys.exit(0)

    # Create FIFO if needed
    if not os.path.exists(FIFO_PATH):
        os.mkfifo(FIFO_PATH)

    btn_up = Button(5, bounce_time=0.05)
    btn_down = Button(6, bounce_time=0.05)
    btn_select = Button(16, bounce_time=0.05)
    btn_back = Button(26, bounce_time=0.05)
    pwr = PowerButton(21)

    btn_up.when_pressed = on_up
    btn_down.when_pressed = on_down
    btn_select.when_pressed = on_select
    btn_back.when_pressed = on_back

    print("GPIO buttons active. Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
