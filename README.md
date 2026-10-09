![screenshot](gpu-manager.png)

cat << 'EOF' | sudo tee /usr/local/bin/gpu-mode > /dev/null
#!/bin/bash

# NVIDIA GPU Performance Manager Backend

if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root/sudo: sudo gpu-mode [on|off|status]"
  exit 1
fi

case "$1" in
  on)
    echo "=== Setting GPU to Maximum Performance Mode ==="
    nvidia-smi -pm 1
    nvidia-smi -pl 80
    nvidia-smi --auto-boost-default=0
    nvidia-smi -ac 7000,1545
    echo "✔ Maximum performance mode activated!"
    ;;
  off)
    echo "=== Resetting GPU to Default Power Mode ==="
    nvidia-smi -acp 0
    nvidia-smi --auto-boost-default=1
    nvidia-smi -pm 0
    echo "✔ Default power management activated!"
    ;;
  status)
    echo "=== Current GPU Power and Clock Status ==="
    nvidia-smi --query-gpu=power.draw,power.limit,clocks.gr,clocks.sm,clocks.mem,temperature.gpu --format=csv
    ;;
  *)
    echo "Usage: sudo gpu-mode {on|off|status}"
    exit 1
    ;;
esac
EOF

sudo chmod +x /usr/local/bin/gpu-mode
