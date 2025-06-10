import tkinter as tk
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x200")
        
        # GUI Elements
        self.label = tk.Label(root, text="Enter seconds:", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.seconds_entry = tk.Entry(root, font=("Arial", 12), width=10)
        self.seconds_entry.pack(pady=5)
        
        self.start_button = tk.Button(root, text="Start Timer", font=("Arial", 12), command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.time_label = tk.Label(root, text="00:00", font=("Arial", 24, "bold"))
        self.time_label.pack(pady=10)
        
        self.is_running = False
        self.remaining_time = 0

    def start_timer(self):
        if self.is_running:
            return
        
        try:
            seconds = int(self.seconds_entry.get())
            if seconds <= 0:
                messagebox.showerror("Error", "Please enter a positive number of seconds.")
                return
            self.remaining_time = seconds
            self.is_running = True
            self.start_button.config(state="disabled")
            self.update_timer()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def update_timer(self):
        if self.is_running and self.remaining_time > 0:
            mins, secs = divmod(self.remaining_time, 60)
            self.time_label.config(text=f"{mins:02d}:{secs:02d}")
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        elif self.remaining_time <= 0:
            self.is_running = False
            self.time_label.config(text="00:00")
            self.start_button.config(state="normal")
            messagebox.showinfo("Timer", "Time's up!")
            # Simulate beep sound with ASCII bell character
            print("\a" * 3)

def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()