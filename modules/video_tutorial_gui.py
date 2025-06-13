import tkinter as tk
from tkinter import ttk
import webbrowser
from modules.video_links import video_data

class VideoTutorials(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,style='Custom.TFrame')
        self.controller = controller
        self.videos = video_data  # ✅ Define the video dictionary

        # 🔍 Search bar
        ttk.Label(self, text="🎥 First-Aid Video Tutorials", font=("Arial", 16)).pack(pady=10)
        ttk.Label(self, text="Click on a topic or search to open the YouTube video").pack(pady=5)

        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self.update_list)

        tk.Label(self, text="🔍 Search Tutorial:").pack(pady=5)
        self.search_entry = tk.Entry(self, textvariable=self.search_var, width=40)
        self.search_entry.pack(pady=5)

        # 📄 Listbox
        self.listbox = tk.Listbox(self, height=12, width=60)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-1>", self.open_video_from_list)

        self.update_list()  # 📝 Load full list initially

        # 🔙 Back Button
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("WelcomeScreen")).pack(pady=10)

    def update_list(self, *args):
        search = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        for title in self.videos:
            if search in title.lower():
                self.listbox.insert(tk.END, title)

    def open_video_from_list(self, event):
        selection = self.listbox.get(tk.ACTIVE)
        if selection in self.videos:
            webbrowser.open(self.videos[selection])

