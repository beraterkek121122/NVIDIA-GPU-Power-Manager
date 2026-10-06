# NVIDIA GPU Power Manager

A sleek, modern Linux desktop utility built with Python and `tkinter` featuring the **Catppuccin Mocha** color palette. Designed to easily toggle NVIDIA GPU performance modes and monitor real-time hardware telemetry using `nvidia-smi` and PolicyKit (`pkexec`), tailored specifically for **Arch Linux** and **Omarchy**.

---

## Features

- **Performance Mode Toggle:** Instantly switch between maximum performance (`on`) and default/balanced power states (`off`) with root privileges via `pkexec`.
- **Real-Time GPU Status Monitor:** Automatically queries `nvidia-smi` to display live hardware statistics:
  - Power Draw / Limit
  - Core Clock Speed
  - Memory Clock Speed
  - GPU Temperature
  - GPU Load (Utilization)
- **Modern UI Design:** Clean, distraction-free interface styled with the popular Catppuccin Mocha dark theme and custom cursor feedback.

---

## Prerequisites & Dependencies (Arch Linux / Omarchy)

To run this application properly on your Arch Linux or Omarchy system, ensure you have the following installed:

1. **Python 3.x** and `tkinter`
2. **NVIDIA Proprietary Drivers** & `nvidia-smi` command-line utility
3. **PolicyKit (`pkexec`)** configured for graphical root password prompts
4. **Backend Script (`/usr/local/bin/gpu-mode`)**: The application executes a privileged backend script to manage GPU power states. Make sure your script exists and is executable:
   ```bash
   sudo chmod +x /usr/local/bin/gpu-mode
   ```

---

## Installation & Setup on Arch Linux / Omarchy

1. **Install required packages via pacman:**
   ```bash
   sudo pacman -S python tk nvidia nvidia-utils polkit
   ```

2. **Clone or Download** the project repository to your local machine:
   ```bash
   git clone https://github.com/your-username/nvidia-gpu-power-manager.git
   cd nvidia-gpu-power-manager
   ```

3. **Ensure the backend script is in place:**
   Make sure `/usr/local/bin/gpu-mode` is created on your Arch/Omarchy system and handles the `on` and `off` arguments correctly with root privileges.

4. **Run the Application:**
   ```bash
   python3 main.py
   ```

---

## Code Structure

```text
├── main.py       # Main GUI application and command handlers
└── README.md     # Project documentation
```

---

## Troubleshooting

- **"Could Not Retrieve GPU Status!"**: This error appears if `nvidia-smi` fails to execute, which usually means NVIDIA drivers are missing, not loaded, or the user lacks permission. Verify your drivers by running `nvidia-smi` in your terminal.
- **Authorization Fails / Cancelled**: Toggling the performance mode requires root privileges. When prompted by `pkexec`, enter your administrator password.

---

## License

This project is open-source and available under the [MIT License](LICENSE).