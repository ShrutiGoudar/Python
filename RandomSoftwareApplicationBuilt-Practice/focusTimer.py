import tkinter as tk

class FocusTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Focus Timer")
        self.root.geometry("300x200")
        self.root.resizable(True, True)

        self.time_left = 0
        self.running = False
        self.focus_minutes = 5

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#4613b4")
        self.input_frame.pack(expand=True, fill="both", padx=20, pady=20)

        tk.Label(self.input_frame, text="Enter focus time (minutes):", 
                font=("Segoe UI", 12), fg="white", bg="#4613b4").pack(pady=10)

        self.entry = tk.Entry(self.input_frame, font=("Segoe UI", 14), justify="center", width=10)
        self.entry.insert(0, str(self.focus_minutes))
        self.entry.pack(pady=10)

        tk.Button(self.input_frame, text="Start Timer", command=self.start_timer, 
                 bg="#049ff3", fg="black", font=("Segoe UI", 12)).pack(pady=10)

        # Timer Frame (hidden initially)
        self.timer_frame = tk.Frame(root, bg="#4613b4")

        self.label = tk.Label(
            self.timer_frame, text="",
            font=("Segoe UI", 55), fg="black", bg="#4613b4"
        )
        self.label.pack(expand=True, fill="both")

        btn_frame = tk.Frame(self.timer_frame, bg="#4a9f26")
        btn_frame.pack(fill="x")

        tk.Button(btn_frame, text="Start", command=self.start).pack(side="left", expand=True)
        tk.Button(btn_frame, text="Pause", command=self.pause).pack(side="left", expand=True)
        tk.Button(btn_frame, text="Reset", command=self.reset).pack(side="left", expand=True)
        tk.Button(btn_frame, text="Change Timer", command=self.change_timer).pack(side="left", expand=True)

        self.root.configure(bg="#4613b4")

    def start_timer(self):
        try:
            self.focus_minutes = int(self.entry.get())
            if self.focus_minutes <= 0:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "25")
                return
        except ValueError:
            return
        
        self.time_left = self.focus_minutes * 60
        self.input_frame.pack_forget()
        self.label.config(text=self.format_time())
        self.timer_frame.pack(expand=True, fill="both")
        self.start()

    def format_time(self):
        m, s = divmod(self.time_left, 60)
        return f"{m:02d}:{s:01d}"

    def update(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.label.config(text=self.format_time())
            self.root.after(1000, self.update)
        elif self.time_left == 0 and self.running:
            self.label.config(text="DONE 🎉")
            self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time_left = self.focus_minutes * 60
        self.label.config(text=self.format_time())

    def change_timer(self):
        self.timer_frame.pack_forget()
        self.input_frame.pack(expand=True, fill="both", padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusTimer(root)
    root.mainloop()
