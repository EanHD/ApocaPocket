#!/bin/bash
# Create a deployment package for SD card transfer
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

# Ensure index is current
echo "Rebuilding index..."
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi
python tools/build_index.py

# Package
OUTDIR="${ROOT}/exports"
mkdir -p "$OUTDIR"
STAMP=$(date +%Y%m%d-%H%M%S)
ARCHIVE="$OUTDIR/fieldnode-${STAMP}.tar.gz"

echo "Creating deployment archive..."
tar czf "$ARCHIVE" \
    --exclude='.venv' \
    --exclude='exports/*.tar*' \
    --exclude='.git' \
    --exclude='__pycache__' \
    -C "$(dirname "$ROOT")" \
    "$(basename "$ROOT")"

SIZE=$(du -sh "$ARCHIVE" | cut -f1)
ENTRIES=$(sqlite3 index/fieldnode.db 'SELECT COUNT(*) FROM entries' 2>/dev/null || echo '?')

echo ""
echo "════════════════════════════════════"
echo "  Deployment package ready"
echo "  Archive: $ARCHIVE"
echo "  Size: $SIZE"
echo "  Entries: $ENTRIES"
echo ""
echo "  Transfer to Pi:"
echo "    scp $ARCHIVE pi@<pi-ip>:~/"
echo "    ssh pi@<pi-ip>"
echo "    tar xzf fieldnode-*.tar.gz"
echo "    cd apocalypse-field-node"
echo "    sudo bash pi/scripts/setup_pi.sh"
echo "════════════════════════════════════"
