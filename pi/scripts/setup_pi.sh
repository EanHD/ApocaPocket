#!/bin/bash
# Apocalypse Field Node — Pi Zero 2 W Setup Script
# Run on fresh Raspberry Pi OS Lite installation
set -euo pipefail

echo "══════════════════════════════════════"
echo "  APOCALYPSE FIELD NODE — Pi Setup"
echo "══════════════════════════════════════"

# ── System updates (minimal) ──────────────────────────
echo "[1/7] Minimal system update..."
sudo apt-get update -qq
sudo apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv sqlite3 \
    python3-gpiozero git

# ── Disable unnecessary services ──────────────────────
echo "[2/7] Disabling unnecessary services..."
sudo systemctl disable --now bluetooth.service 2>/dev/null || true
sudo systemctl disable --now avahi-daemon.service 2>/dev/null || true
sudo systemctl disable --now triggerhappy.service 2>/dev/null || true
sudo systemctl disable --now wpa_supplicant.service 2>/dev/null || true
# WiFi and BT hardware off
sudo rfkill block wifi 2>/dev/null || true
sudo rfkill block bluetooth 2>/dev/null || true

# ── Create application directory ──────────────────────
echo "[3/7] Setting up application..."
APP_DIR="/opt/fieldnode"
sudo mkdir -p "$APP_DIR"
sudo cp -r "$(dirname "$0")/../.." "$APP_DIR/"
sudo chown -R pi:pi "$APP_DIR"

# ── Python venv ───────────────────────────────────────
echo "[4/7] Setting up Python environment..."
cd "$APP_DIR"
python3 -m venv .venv
source .venv/bin/activate
pip install --quiet pyyaml

# ── Build database ────────────────────────────────────
echo "[5/7] Building search index..."
python tools/build_index.py

# ── Configure auto-start ──────────────────────────────
echo "[6/7] Configuring auto-start service..."
sudo tee /etc/systemd/system/fieldnode.service > /dev/null << 'EOF'
[Unit]
Description=Apocalypse Field Node
After=multi-user.target

[Service]
Type=simple
User=pi
WorkingDirectory=/opt/fieldnode
Environment=TERM=linux
Environment=ESCDELAY=25
ExecStart=/opt/fieldnode/.venv/bin/python /opt/fieldnode/pi/interface/fieldnode_tui.py
StandardInput=tty
StandardOutput=tty
TTYPath=/dev/tty1
TTYReset=yes
TTYVHangup=yes
TTYVTDisallocate=yes
Restart=on-failure
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable fieldnode.service

# ── Boot optimizations ────────────────────────────────
echo "[7/7] Applying boot optimizations..."

# Reduce boot time
sudo tee -a /boot/config.txt > /dev/null << 'BOOTCFG'

# ── Field Node optimizations ──
disable_splash=1
boot_delay=0
dtoverlay=disable-bt
# GPU memory minimum (headless or small display)
gpu_mem=16
# Overclock (conservative, safe for Pi Zero 2 W)
arm_freq=1200
over_voltage=4
BOOTCFG

# Reduce kernel verbosity
if ! grep -q "quiet" /boot/cmdline.txt; then
    sudo sed -i 's/$/ quiet loglevel=3/' /boot/cmdline.txt
fi

# Auto-login to tty1
sudo mkdir -p /etc/systemd/system/getty@tty1.service.d
sudo tee /etc/systemd/system/getty@tty1.service.d/autologin.conf > /dev/null << 'AUTOLOGIN'
[Service]
ExecStart=
ExecStart=-/sbin/agetty --autologin pi --noclear %I $TERM
AUTOLOGIN

echo ""
echo "══════════════════════════════════════"
echo "  Setup complete!"
echo ""
echo "  Database: $(sqlite3 /opt/fieldnode/index/fieldnode.db 'SELECT COUNT(*) FROM entries') entries"
echo "  Service:  fieldnode.service (enabled)"
echo ""
echo "  Reboot to start: sudo reboot"
echo "══════════════════════════════════════"
