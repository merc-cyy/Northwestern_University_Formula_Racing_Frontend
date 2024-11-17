import customtkinter as ctk

class FourFramesApp(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("dark")
        super().__init__()
        self.title("Four Frames")
        self.geometry("800x600")
        self.create_layout()

    def create_layout(self):
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        # Create two rows for the frames
        top_row = ctk.CTkFrame(container)
        bottom_row = ctk.CTkFrame(container)

        # Pack the rows equally in the parent container
        top_row.pack(side="top", fill="both", expand=True)
        bottom_row.pack(side="top", fill="both", expand=True)

        self.frame1 = ctk.CTkFrame(top_row, corner_radius=10, border_width=2, border_color="blue")
        self.frame2 = ctk.CTkFrame(top_row, corner_radius=10, border_width=2, border_color="red")
        self.frame3 = ctk.CTkFrame(bottom_row, corner_radius=10, border_width=2, border_color="green")
        self.frame4 = ctk.CTkFrame(bottom_row, corner_radius=10, border_width=2, border_color="purple")

        self.frame1.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.frame2.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.frame3.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.frame4.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        ctk.CTkLabel(self.frame1, text="Frame 1", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(self.frame2, text="Frame 2", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(self.frame3, text="Frame 3", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(self.frame4, text="Frame 4", font=("Arial", 16)).pack(pady=10)

# Run the application
if __name__ == "__main__":
    app = FourFramesApp()
    app.mainloop()
