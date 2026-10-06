import tkinter as tk
from tkinter import messagebox
import subprocess

class GPUManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NVIDIA GPU Performance Hub")
        self.root.geometry("420x450")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        # Başlık
        title_label = tk.Label(
            root, 
            text="GPU\nPOWER MANAGER",
            font=("Segoe UI", 16, "bold"), 
            fg="#cdd6f4", 
            bg="#1e1e2e"
        )
        title_label.pack(pady=(20, 15))

        # Performans Aç Butonu
        self.btn_on = tk.Button(
            root, 
            text="⚡ PERFORMANCE MOD (ON)",
            font=("Segoe UI", 11, "bold"), 
            bg="#a6e3a1", 
            fg="#11111b", 
            activebackground="#94e2d5",
            cursor="hand2",
            command=lambda: self.run_command("on")
        )
        self.btn_on.pack(fill="x", padx=40, pady=8, ipady=8)

        # Varsayılan Mod Butonu
        self.btn_off = tk.Button(
            root, 
            text="🌱 DEFAULT MOD (OFF)",
            font=("Segoe UI", 11, "bold"), 
            bg="#f38ba8", 
            fg="#11111b", 
            activebackground="#f5e0dc",
            cursor="hand2",
            command=lambda: self.run_command("off")
        )
        self.btn_off.pack(fill="x", padx=40, pady=8, ipady=8)

        # Durum Yenile Butonu
        self.btn_status = tk.Button(
            root, 
            text="🔄 REFRESH STATUS",
            font=("Segoe UI", 10), 
            bg="#89b4fa", 
            fg="#11111b", 
            activebackground="#b4befe",
            cursor="hand2",
            command=self.update_status
        )
        self.btn_status.pack(fill="x", padx=40, pady=(8, 15), ipady=5)

        # Durum Ekranı Frame
        status_frame = tk.LabelFrame(
            root, 
            text=" Real-time GPU Status ",
            font=("Segoe UI", 10, "bold"), 
            fg="#bac2de", 
            bg="#181825", 
            bd=1, 
            relief="solid"
        )
        status_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.status_label = tk.Label(
            status_frame, 
            text="Loading...",
            font=("Consolas", 9), 
            fg="#a6adc8", 
            bg="#181825", 
            justify="left",
            anchor="nw"
        )
        self.status_label.pack(fill="both", expand=True, padx=10, pady=10)

        # İlk Açılışta Durumu Getir
        self.update_status()

    def run_command(self, mode):
        try:
            # pkexec kullanarak root şifresi penceresi açar
            cmd = f"pkexec /usr/local/bin/gpu-mode {mode}"
            result = subprocess.run(
                cmd, 
                shell=True, 
                capture_output=True, 
                text=True, 
                check=True
            )
            out_msg = result.stdout.strip() if result.stdout.strip() else f"Mod {mode.upper()} Activated!"
            messagebox.showinfo("Successful", out_msg)
            self.update_status()
        except Exception as e:
            messagebox.showerror("Error", "The operation was cancelled or authorization could not be verified.")

    def update_status(self):
        try:
            cmd = "nvidia-smi --query-gpu=power.draw,power.limit,clocks.gr,clocks.mem,temperature.gpu,utilization.gpu --format=csv,noheader"
            output = subprocess.check_output(cmd, shell=True, text=True).strip()
            
            data = [x.strip() for x in output.split(",")]
            status_text = (
                f" Use of Force : {data[0]} / {data[1]}\n"
                f" Core Speed : {data[2]}\n"
                f" Memory Speed   : {data[3]}\n"
                f" Heat      : {data[4]}\n"
                f" GPU Load      : {data[5]}"
            )
            self.status_label.config(text=status_text, fg="#a6e3a1")
        except Exception:
            self.status_label.config(text="Could Not Retrieve GPU Status!", fg="#f38ba8")

if __name__ == "__main__":
    root = tk.Tk()
    app = GPUManagerApp(root)
    root.mainloop()
