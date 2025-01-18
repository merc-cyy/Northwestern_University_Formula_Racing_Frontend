import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

NU_PURPLE_HEX = "#4E2A84"

class MultiFrameApp(ctk.CTk):
    def __init__(self) -> None:
        ctk.set_appearance_mode("dark")
        super().__init__()
        self.title("Multi-Frame System")
        self.geometry("900x700")


        # current active layout
        self.current_layout = None
        self.current_layout_button = None
        self.current_graph_button = None

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

        # layout frame
        self.layout_frame = ctk.CTkFrame(self.side_bar, width=100)
        self.layout_frame.pack(side='top', pady=(0,10))
        self.master_layout_button = ctk.CTkButton(self.layout_frame, text="Layout", command=self.layout_show, fg_color=NU_PURPLE_HEX)
        self.master_layout_button.pack(pady=10, padx=10, fill="x")

        #graph choices frame
        self.graph_frame = ctk.CTkFrame(self.side_bar, width=100)
        self.graph_frame.pack(side='top')
        self.master_graph_button = ctk.CTkButton(self.graph_frame, text="Graphs", command=self.graph_show, fg_color=NU_PURPLE_HEX)
        self.master_graph_button.pack(pady=10, padx=10, fill="x")

        #graph state
        self.bar_graph_state = None
        
        self.show_four_frames()

    def layout_show(self):#display layout buttons
            if self.current_layout_button == "layout displayed":
                self.clear_layout_buttons()
                return
            self.current_layout_button = "layout displayed"
    
            ctk.CTkButton(self.layout_frame, text="1-Frame Layout", fg_color= "#DADADA", text_color='black', command=self.show_one_frame).pack(pady=10, padx=10, fill="x")
            ctk.CTkButton(self.layout_frame, text="2-Frame Layout", fg_color= "#DADADA", text_color='black', command=self.show_two_frames).pack(pady=10, padx=10, fill="x")
            ctk.CTkButton(self.layout_frame, text="3-Frame Layout", fg_color= "#DADADA", text_color='black', command=self.show_three_frames).pack(pady=10, padx=10, fill="x")
            ctk.CTkButton(self.layout_frame, text="4-Frame Layout", fg_color= "#DADADA", text_color='black', command=self.show_four_frames).pack(pady=10, padx=10, fill="x")
           

    def clear_layout_buttons(self):
        for widget in self.layout_frame.winfo_children():
            if widget != self.master_layout_button:
                widget.destroy()
        self.current_layout_button = None


    def graph_show(self):#display graph buttons
        if self.current_graph_button == "graph choices displayed":
                self.clear_graph_buttons()
                return
        self.current_graph_button = "graph choices displayed"

        ctk.CTkButton(self.graph_frame, text="Line Graph", fg_color= 'light blue', text_color='black', command=self.display_graph).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.graph_frame, text="Pie Chart", fg_color= 'light blue', text_color='black', command=self.display_graph).pack(pady=10, padx=10, fill="x")
        ctk.CTkButton(self.graph_frame, text="Bar Graph", fg_color= 'light blue', text_color='black', command=self.display_graph).pack(pady=10, padx=10, fill="x")

 
            
    def clear_graph_buttons(self):
        for widget in self.graph_frame.winfo_children():
            if widget != self.master_graph_button:
                widget.destroy()
        self.current_graph_button = None


    def show_one_frame(self):
        if self.current_layout == "1-frame":
            return  
        self.current_layout = "1-frame"
        self.clear_main_content()

        frame = ctk.CTkFrame(self.main_content, corner_radius=10, border_width=2, border_color=NU_PURPLE_HEX)
        frame.pack(fill="both", expand=True, padx=5, pady=5)

        ctk.CTkLabel(frame, text="Single Frame", font=("Arial", 16)).pack(pady=10)

    def show_two_frames(self):
        if self.current_layout == "2-frame":
            return 
        self.current_layout = "2-frame"
        self.clear_main_content()

        self.frame1 = ctk.CTkFrame(self.main_content, corner_radius=10, border_width=2, border_color=NU_PURPLE_HEX)
        self.frame2 = ctk.CTkFrame(self.main_content, corner_radius=10, border_width=2, border_color="white")

        self.frame1.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.frame2.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        ctk.CTkLabel(self.frame1, text="Frame A", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(self.frame2, text="Frame B", font=("Arial", 16)).pack(pady=10)

    def show_three_frames(self):
        if self.current_layout == "3-frame":
            return  
        self.current_layout = "3-frame"
        self.clear_main_content()

        left_frame = ctk.CTkFrame(self.main_content, corner_radius=10, border_width=2, border_color=NU_PURPLE_HEX)
        right_container = ctk.CTkFrame(self.main_content)

        left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        right_container.pack(side="right", fill="both", expand=True)

        top_right_frame = ctk.CTkFrame(right_container, corner_radius=10, border_width=2, border_color="white")
        bottom_right_frame = ctk.CTkFrame(right_container, corner_radius=10, border_width=2, border_color="silver")

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

        self.frame1 = ctk.CTkFrame(top_row, corner_radius=10, border_width=2, border_color=NU_PURPLE_HEX)
        self.frame2 = ctk.CTkFrame(top_row, corner_radius=10, border_width=2, border_color="white")
        self.frame3 = ctk.CTkFrame(bottom_row, corner_radius=10, border_width=2, border_color="white")
        self.frame4 = ctk.CTkFrame(bottom_row, corner_radius=10, border_width=2, border_color=NU_PURPLE_HEX)

        self.frame1.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.frame2.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.frame3.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.frame4.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        ctk.CTkLabel(self.frame1, text="Frame 1", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(self.frame2, text="Frame 2", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(self.frame3, text="Frame 3", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(self.frame4, text="Frame 4", font=("Arial", 16)).pack(pady=10)

    def clear_main_content(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    #PLOTTING
    def bar_graph(self, file_path, x_col=None, y_col=None):
        if self.bar_graph_state == "Bar Graph displayed":
            return
        else:    
            self.bar_graph_state = "Bar Graph displayed"#to avaoid multiple graphs
            data = pd.read_csv(file_path)
            print("Data Loaded Successfully!")

            # Check for required columns
            if x_col not in list(data.columns) or y_col not in list(data.columns):
                raise ValueError(f"Specified columns '{x_col}' or '{y_col}' not found in the CSV file.")
            
            frame_bg = (0.2,0.2,0.2)

            # Create a Matplotlib figure
            fig, ax = plt.subplots()
            fig.patch.set_facecolor(frame_bg)  # Set figure background to match frame

            # Customize plot appearance
            ax.set_facecolor(frame_bg)  # Set axes background
            ax.bar(data[x_col], data[y_col], color=NU_PURPLE_HEX)  # Bar color

            # Set label, title, and grid colors
            ax.set_xlabel(x_col, color="white")
            ax.set_ylabel(y_col, color="white")
            ax.set_title("Testing Title", color="white")

            # Set tick colors
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')

            # Remove spines or set them to white
            for spine in ax.spines.values():
                spine.set_color("white")

            bar_image_path = "Graphs/TestBarGraph.png"
            fig.savefig(bar_image_path)
            plt.close()
            return bar_image_path

    def display_image_on_frame(self, frame: ctk.CTkFrame, image_path=None):
            image = Image.open(image_path)
            tk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(285, 285))
            label = ctk.CTkLabel(frame, image=tk_image, text="", width=0, height = 0)
            label.image = tk_image  # Keep a reference to avoid garbage collection
            frame.pack_propagate(False) # prevents frame from expanding when image is packed
            label.pack(fill ="none", padx = 0, pady = 0)


    def display_graph(self):
        path = 'dummy.csv'
        graph_image = self.bar_graph(path, "name", "amount")
        
        #to display on frame1
        self.display_image_on_frame(self.frame1, graph_image)

# Run the application
if __name__ == "__main__":
    app = MultiFrameApp()
    app.mainloop()


#Notes: 
"""
So when you call the bar graph fucntion it displays on each child on the main content (however the main content has two containers that's why its displaying on two frames)
"""
