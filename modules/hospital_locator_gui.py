# modules/hospital_locator_gui.py

import tkinter as tk
from tkinter import ttk
import webbrowser

class HospitalLocator(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="🏥 Hospital Locator", font=("Arial", 16)).pack(pady=10)

        ttk.Label(self, text="Enter your city or location:").pack()
        self.location_entry = ttk.Entry(self, width=50)
        self.location_entry.pack(pady=5)

        ttk.Button(self, text="Search Nearest Hospitals", command=self.search_hospitals).pack(pady=10)

        # Remove: from main_app import WelcomeScreen
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("WelcomeScreen")).pack()


    def search_hospitals(self):
        location = self.location_entry.get().strip()
        if location:
            url = f"https://www.google.com/maps/search/hospitals+near+{location.replace(' ', '+')}"
            webbrowser.open(url)
        else:
            from tkinter import messagebox
            messagebox.showwarning("Input Required", "Please enter a location.")
