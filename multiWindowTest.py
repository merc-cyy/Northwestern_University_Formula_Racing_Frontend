import customtkinter as ctk

class MultiFrameApp(ctk.CTk):
    def __init__(self) -> None:
        ctk.set_appearance_mode("dark")
        super().__init__()
        self.title("Multi-Frame System")
        self.geometry("900x700")

        # current active layout
        self.current_layout = None

        self.create_layout()

    def create_layout(self):
        # main container
        main_container = ctk.CTkFrame(self)
        main_container.pack(fill="both", expand=True)

        # side option bar
        self.side_bar = ctk.CTkFrame(main_container, width=150, corner_radius=0)
        self.side_bar.pack(side="left", fill="y")

        # main content
        self.main_content = ctk.CTkFrame(main_container)
        self.main_content.pack(side="right", fill="both", expand=True)

        # toggle buttons
        ctk.CTkButton(self.side_bar, text="1-Frame Layout", command=self.show_one_frame).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.side_bar, text="2-Frame Layout", command=self.show_two_frames).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.side_bar, text="3-Frame Layout", command=self.show_three_frames).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.side_bar, text="4-Frame Layout", command=self.show_four_frames).pack(pady=10, padx=10, fill="x")

        self.show_four_frames()

    def show_one_frame(self):
        if self.current_layout == "1-frame":
            return  
        self.current_layout = "1-frame"
        self.clear_main_content()

        frame = ctk.CTkFrame(self.main_content, corner_radius=10, border_width=2, border_color="blue")
        frame.pack(fill="both", expand=True, padx=5, pady=5)

        ctk.CTkLabel(frame, text="Single Frame", font=("Arial", 16)).pack(pady=10)

    def show_two_frames(self):
        if self.current_layout == "2-frame":
            return 
        self.current_layout = "2-frame"
        self.clear_main_content()

        frame1 = ctk.CTkFrame(self.main_content, corner_radius=10, border_width=2, border_color="blue")
        frame2 = ctk.CTkFrame(self.main_content, corner_radius=10, border_width=2, border_color="red")

        frame1.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        frame2.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        ctk.CTkLabel(frame1, text="Frame A", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(frame2, text="Frame B", font=("Arial", 16)).pack(pady=10)

    def show_three_frames(self):
        if self.current_layout == "3-frame":
            return  
        self.current_layout = "3-frame"
        self.clear_main_content()

        left_frame = ctk.CTkFrame(self.main_content, corner_radius=10, border_width=2, border_color="blue")
        right_container = ctk.CTkFrame(self.main_content)

        left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        right_container.pack(side="right", fill="both", expand=True)

        top_right_frame = ctk.CTkFrame(right_container, corner_radius=10, border_width=2, border_color="red")
        bottom_right_frame = ctk.CTkFrame(right_container, corner_radius=10, border_width=2, border_color="green")

        top_right_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        bottom_right_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        ctk.CTkLabel(left_frame, text="Big Frame", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(top_right_frame, text="Top Right Frame", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(bottom_right_frame, text="Bottom Right Frame", font=("Arial", 16)).pack(pady=10)

    def show_four_frames(self):
        if self.current_layout == "4-frame":
            return  
        self.current_layout = "4-frame"
        self.clear_main_content()

        # Create a four-frame layout
        top_row = ctk.CTkFrame(self.main_content)
        bottom_row = ctk.CTkFrame(self.main_content)

        top_row.pack(side="top", fill="both", expand=True)
        bottom_row.pack(side="top", fill="both", expand=True)

        frame1 = ctk.CTkFrame(top_row, corner_radius=10, border_width=2, border_color="blue")
        frame2 = ctk.CTkFrame(top_row, corner_radius=10, border_width=2, border_color="red")
        frame3 = ctk.CTkFrame(bottom_row, corner_radius=10, border_width=2, border_color="green")
        frame4 = ctk.CTkFrame(bottom_row, corner_radius=10, border_width=2, border_color="purple")

        frame1.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        frame2.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        frame3.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        frame4.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        ctk.CTkLabel(frame1, text="Frame 1", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(frame2, text="Frame 2", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(frame3, text="Frame 3", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(frame4, text="Frame 4", font=("Arial", 16)).pack(pady=10)

    def clear_main_content(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()


# Run the application
if __name__ == "__main__":
    app = MultiFrameApp()
    app.mainloop()
