### NFR DAQ Interface Main Program ###
import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
                                    width=300,
                                    height=50,
                                    command=self.test_func)
        self.button.place(relx=0.5,rely=0.5)
        self.root.mainloop()

    def test_func(self) -> None:
        self.text = ctk.CTkTextbox(master = self.root,
                                   width=300,
                                   height=50
                                   )
        self.text.place(relx = 0.4, rely = 0.8)
        self.root.update()

if __name__ == "__main__":
    app = DAQInterface()
