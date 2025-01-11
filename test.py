import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

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
        self.master_layout_button = ctk.CTkButton(self.layout_frame, text="Layout", command=self.layout_show)
        self.master_layout_button.pack(pady=10, padx=10, fill="x")

        #graph choices frame
        self.graph_frame = ctk.CTkFrame(self.side_bar, width=100)
        self.graph_frame.pack(side='top')
        self.master_graph_button = ctk.CTkButton(self.graph_frame, text="Graphs", command=self.graph_show)
        self.master_graph_button.pack(pady=10, padx=10, fill="x")

        #graph state
        self.bar_graph_state = None
        
        self.show_four_frames()

    def layout_show(self):#display layout buttons
            if self.current_layout_button == "layout displayed":
                self.clear_layout_buttons()
                return
            self.current_layout_button = "layout displayed"
    
            ctk.CTkButton(self.layout_frame, text="1-Frame Layout", fg_color= 'light blue', text_color='black', command=self.show_one_frame).pack(pady=10, padx=10, fill="x")
            ctk.CTkButton(self.layout_frame, text="2-Frame Layout", fg_color= 'light blue', text_color='black', command=self.show_two_frames).pack(pady=10, padx=10, fill="x")
            ctk.CTkButton(self.layout_frame, text="3-Frame Layout", fg_color= 'light blue', text_color='black', command=self.show_three_frames).pack(pady=10, padx=10, fill="x")
            ctk.CTkButton(self.layout_frame, text="4-Frame Layout", fg_color= 'light blue', text_color='black', command=self.show_four_frames).pack(pady=10, padx=10, fill="x")
           

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

    #PLOTTING
    def bar_graph(self, file_path, x_col=None, y_col=None):
        if self.bar_graph_state == "Bar Graph displayed":
            return
        else:    
            self.bar_graph_state = "Bar Graph displayed"#to avaoid multiple graphs
            data = pd.read_csv(file_path, header=None)
            print("Data Loaded Successfully!")

            # Check for required columns
            # if x_col not in data.columns or y_col not in data.columns:
            #     raise ValueError(f"Specified columns '{x_col}' or '{y_col}' not found in the CSV file.")
            
            plt.bar(data[x_col], data[y_col], color='blue')
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title("Testing title")
            plt.savefig("TestBarGraph.png")
            bar_image_path = "TestBarGraph.png"
            plt.close()

            return bar_image_path

    def display_image_on_frame(self, frame, image_path=None):
            image = Image.open(image_path)
            tk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(300, 300))
            label = ctk.CTkLabel(frame, image=tk_image, text="")
            label.image = tk_image  # Keep a reference to avoid garbage collection
            label.pack(fill="both")


    def display_graph(self):
        path = 'time.csv'
        graph_image = self.bar_graph(path, 0, 1)
        
        #to display on all frames
        for fr in self.main_content.winfo_children():
            self.display_image_on_frame(fr, graph_image)

# Run the application
if __name__ == "__main__":
    app = MultiFrameApp()
    app.mainloop()


#Notes: 
"""
So when you call the bar graph fucntion it displays on each child on the main content (however the main content has two containers that's why its displaying on two frames)
"""
