### NFR DAQ Interface Main Program ###
import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from multiWindowTest import MultiFrameApp
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
                                  text="Start",
                                  font=('Arial', 40),
                                  text_color="white",
                                  fg_color=NU_PURPLE_HEX,
                                  corner_radius=20,
                                  width=250,
                                  height=40,
                                  command=self.load_file)
        load_data.pack()
    
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
            
class DAQInterface:
    def __init__(self) -> None:
        ctk.set_appearance_mode("dark")
        self.root = ctk.CTk()
        self.root.geometry("800x500")
        self.root.title("NFR DAQ Interface")
        self.root.update()
        self.button = ctk.CTkButton(master = self.root,
                                    text="Welcome to DAQ",
                                    command=self.create_graph_app)
        self.button.place(relx=0.5,rely=0.5, anchor="center", relwidth=0.15, relheight = 0.1)
        self.root.mainloop()

    def test_func(self) -> None:
        self.text = ctk.CTkTextbox(master = self.root)
        self.text.place(relx = 0.5, rely = 0.8, anchor="center", relwidth = 0.7, relheight= 0.4)
        self.root.update()

    def create_graph_app(self):
        # Create a new window for GraphApp
        graph_window = ctk.CTkToplevel(self)
        graph_window.title("Graph Application")
        graph_window.geometry("800x600")
        
        # Instantiate GraphApp in the new window
        graph_app = MultiFrameApp()

if __name__ == "__main__":
    app = DAQInterface()
    app.mainloop()