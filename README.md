![screenshot](gpu-manager.png)

# NVIDIA GPU Power Manager

A sleek, modern Linux desktop utility built with Python and `tkinter` featuring the **Catppuccin Mocha** color palette. Designed to easily toggle NVIDIA GPU performance modes and monitor real-time hardware telemetry using `nvidia-smi` and PolicyKit (`pkexec`), tailored specifically for **Arch Linux**, **CachyOS**, and **Omarchy**.

---

## Features

- **Performance Mode Toggle:** Instantly switch between maximum performance (`on`) and default/balanced power states (`off`) with root privileges via `pkexec`.
- **Real-Time GPU Telemetry:** Automatically queries `nvidia-smi` to display live hardware statistics:
  - Power Draw / Limit
  - Core Clock Speed
  - Memory Clock Speed
  - GPU Temperature
  - GPU Load (Utilization)
- **Modern UI Design:** Clean, distraction-free interface styled with the popular Catppuccin Mocha dark theme and custom cursor feedback.

---

## Prerequisites & Dependencies

To run this application properly on your Arch Linux / CachyOS / Omarchy system, ensure you have the following installed:

1. **Python 3.x** and `tk` (`tkinter`)
2. **NVIDIA Proprietary Drivers** & `nvidia-smi` command-line utility
3. **PolicyKit (`polkit`)**: Required for graphical root password prompts (`pkexec`)

---

## Installation & Setup

### 1. Install Required System Dependencies

Run the following command in your terminal:

```bash
sudo pacman -S python tk nvidia-utils polkit
