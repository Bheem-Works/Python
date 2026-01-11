import tkinter as tk
from tkinter import messagebox

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Pomodoro Timer")
        self.root.geometry("400x350")
        self.root.configure(bg="#f0f0f0")

        self.time_left = 1500  # Default 25 minutes
        self.running = False
        self.timer_id = None

        # Title Label
        self.title_label = tk.Label(root, text="Pomodoro Timer", font=("Helvetica", 20), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=10)

        # Timer Display
        self.label = tk.Label(root, text="25:00", font=("Helvetica", 60, "bold"), bg="#f0f0f0", fg="#e74c3c")
        self.label.pack(pady=20)

        # Control Buttons Frame
        self.btn_frame = tk.Frame(root, bg="#f0f0f0")
        self.btn_frame.pack(pady=10)

        self.start_btn = tk.Button(self.btn_frame, text="Start", command=self.start_timer, width=8, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"))
        self.start_btn.grid(row=0, column=0, padx=5)

        self.pause_btn = tk.Button(self.btn_frame, text="Pause", command=self.pause_timer, width=8, bg="#f1c40f", fg="white", font=("Arial", 10, "bold"))
        self.pause_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(self.btn_frame, text="Reset", command=self.reset_timer, width=8, bg="#e67e22", fg="white", font=("Arial", 10, "bold"))
        self.reset_btn.grid(row=0, column=2, padx=5)

        # Mode Selection Frame
        self.mode_frame = tk.Frame(root, bg="#f0f0f0")
        self.mode_frame.pack(pady=20)

        tk.Button(self.mode_frame, text="Pomodoro (25m)", command=lambda: self.set_time(25)).pack(side=tk.LEFT, padx=5)
        tk.Button(self.mode_frame, text="Short Break (5m)", command=lambda: self.set_time(5)).pack(side=tk.LEFT, padx=5)
        tk.Button(self.mode_frame, text="Long Break (15m)", command=lambda: self.set_time(15)).pack(side=tk.LEFT, padx=5)

    def set_time(self, minutes):
        self.pause_timer()
        self.time_left = minutes * 60
        self.update_display()

    def update_display(self):
        mins, secs = divmod(self.time_left, 60)
        self.label.config(text=f"{mins:02d}:{secs:02d}")

    def start_timer(self):
        if not self.running:
            self.running = True
            self.countdown()

    def pause_timer(self):
        self.running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

    def reset_timer(self):
        self.pause_timer()
        self.time_left = 1500
        self.update_display()

    def countdown(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.update_display()
            self.timer_id = self.root.after(1000, self.countdown)
        elif self.time_left == 0:
            self.running = False
            messagebox.showinfo("Pomodoro", "Time's up!")
            self.reset_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()