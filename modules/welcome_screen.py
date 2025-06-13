import tkinter as tk
from tkinter import ttk

class WelcomeScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,style='Custom.TFrame')
        self.controller = controller

        # Set background color
        self.configure(style="Welcome.TFrame")

        # Add style
        style = ttk.Style()
        style.configure("Welcome.TFrame", background="#e0f7fa")  # Light teal background
        style.configure("Welcome.TLabel", background="#e0f7fa", font=("Arial", 20))
        style.configure("Welcome.TButton", font=("Arial", 12))

        # Center Frame
        center_frame = ttk.Frame(self, style="Welcome.TFrame")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Animated welcome messages
        self.messages = [
            "Welcome to Emergency Medical Assistant 🩺",
            "Your personal health support system 🚑",
            "Check symptoms, locate hospitals, watch tutorials 🎥",
            "Stay safe. Stay informed. 💡"
        ]
        self.label = ttk.Label(center_frame, text="", style="Welcome.TLabel")
        self.label.pack(pady=10)

        # Buttons
        ttk.Button(center_frame, text="Symptom Checker", style="Welcome.TButton",
                   command=lambda: controller.show_frame("SymptomChecker")).pack(pady=5)

        ttk.Button(center_frame, text="Video Tutorials", style="Welcome.TButton",
                   command=lambda: controller.show_frame("VideoTutorials")).pack(pady=5)

        ttk.Button(center_frame, text="Hospital Locator", style="Welcome.TButton",
                   command=lambda: controller.show_frame("HospitalLocator")).pack(pady=5)

        ttk.Button(center_frame, text="Exit", style="Welcome.TButton", command=controller.quit).pack(pady=15)

        # Start animation
        self.message_index = 0
        self.animate_messages()

    def animate_messages(self):
        current = self.messages[self.message_index]
        self.animate_typing(current, 0)

    def animate_typing(self, message, i):
        if i <= len(message):
            self.label.config(text=message[:i])
            self.after(50, lambda: self.animate_typing(message, i + 1))
        else:
            self.after(2000, self.next_message)  # Wait 2 sec before next

    def next_message(self):
        self.message_index = (self.message_index + 1) % len(self.messages)
        self.animate_messages()
