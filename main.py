### NFR DAQ Interface Main Program ###
import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from test import MultiFrameApp
import time

"""
App Features

- architecture
  - matplotlib (graphs) and customtkinter (GUI)
- custom windows
  - how to accomplish? Anthony
- displaying graphs
- data storage
- live data (feedback says we will wait on this)

"""
# Constants
NU_PURPLE_HEX = "#4E2A84"

class DAQInterface(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        ctk.set_appearance_mode('dark')
        self.title("NFR DAQ Interface")
        self.geometry("900x700")
        self.data_file_path = None
        self.create_app()

    def create_app(self):
        self.title_screen = ctk.CTkFrame(self)
        self.title_screen.pack(fill='both', expand=True)

        title = ctk.CTkLabel(self.title_screen, 
                             text="NFR 25 DAQ Interface", 
                             font=('Arial', 64),
                             text_color="white",
                             corner_radius=10)
        title.pack(padx = 25, pady = 50)

        start_button = ctk.CTkButton(self.title_screen,
                                     text="Start",
                                     font=('Arial', 40),
                                     text_color="white",
                                     fg_color=NU_PURPLE_HEX,
                                     corner_radius=20,
                                     width=250,
                                     height=40,
                                     command=self.configuration)
        start_button.pack(padx = 25, pady = 25)

    def configuration(self):
        time.sleep(0.4)
        self.title_screen.destroy()

        self.config_screen = ctk.CTkFrame(self)
        self.config_screen.pack(fill='both', expand=True)

        header = ctk.CTkLabel(self.config_screen, 
                             text="Configure Interface", 
                             font=('Arial', 64),
                             text_color="white",
                             corner_radius=10)
        header.pack(padx = 25, pady = 50)

        self.file_label = ctk.CTkLabel(self.config_screen, 
                                       text="Select a file.",
                                       font=("Arial",24))
        self.file_label.pack(pady = 20)

        load_data = ctk.CTkButton(self.config_screen,
                                  text="Load Data",
                                  font=('Arial', 24),
                                  text_color="white",
                                  fg_color=NU_PURPLE_HEX,
                                  corner_radius=20,
                                  width=250,
                                  height=40,
                                  command=self.load_file)
        load_data.pack()

        launch_button = ctk.CTkButton(self.config_screen,
                                  text="Launch Interface",
                                  font=('Arial', 40),
                                  text_color="white",
                                  fg_color=NU_PURPLE_HEX,
                                  corner_radius=20,
                                  width=250,
                                  height=40,
                                  command=self.launch_interface)
        
        launch_button.pack(pady = 50)

    def launch_interface(self):
        if self.data_file_path:
            time.sleep(0.4)
            self.config_screen.destroy()
            self.app = MultiFrameApp()
            self.app.mainloop()
    
    def load_file(self):
        # Open a file dialog to select a file
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")]
        )

        # Update the label with the selected file path or show "No file selected" if canceled
        if file_path:
            self.file_label.configure(text=f"Selected File: {file_path}")
        else:
            self.file_label.configure(text="No file selected")

        self.data_file_path = file_path


if __name__ == "__main__":
    app = DAQInterface()
    app.mainloop()