### NFR DAQ Interface Main Program ###
import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from test import MultiFrameApp

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