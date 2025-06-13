import tkinter as tk
from tkinter import ttk

from modules.welcome_screen import WelcomeScreen
from modules.symptom_checker import SymptomChecker
from modules.video_tutorial_gui import VideoTutorials
from modules.hospital_locator_gui import HospitalLocator

class MedicalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Emergency Medical Assistant")

        # 👇 TEMP: Comment fullscreen and use fixed size for better design layout
        # self.attributes("-fullscreen", True)
        self.geometry("900x600")
        self.resizable(False, False)

        self.configure(bg="white")

        self.apply_global_style()

        self.frames = {}
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        self.screen_classes = [WelcomeScreen, SymptomChecker, VideoTutorials, HospitalLocator]

        for ScreenClass in self.screen_classes:
            frame = ScreenClass(parent=container, controller=self)
            self.frames[ScreenClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomeScreen")

        self.protocol("WM_DELETE_WINDOW", self.confirm_exit)

    def apply_global_style(self):
        style = ttk.Style()
        style.theme_use('default')  # You can also try 'clam', 'alt', etc.

        # Apply background color to Frame, Label, and Button
        style.configure('TFrame', background='#f0f8ff')  # Light blue
        style.configure('TLabel', background='#f0f8ff', font=('Helvetica', 11))
        style.configure('TButton', background='#e0f7fa', padding=6, relief="flat", font=('Helvetica', 10))

        # Optionally create a custom frame style
        style.configure('Custom.TFrame', background='#f0f8ff')

    def show_frame(self, screen_name):
        frame = self.frames[screen_name]
        frame.tkraise()

    def confirm_exit(self):
        from tkinter import messagebox
        if messagebox.askokcancel("Exit", "Do you really want to exit the app?"):
            self.destroy()


if __name__ == "__main__":
    app = MedicalApp()
    app.mainloop()
