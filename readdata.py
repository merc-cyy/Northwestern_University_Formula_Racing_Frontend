import pandas as pd
import matplotlib.pyplot as plt

def bar_graph(file_path, x_col=None, y_col=None):
        data = pd.read_csv(file_path, header=None)
        print("Data Loaded Successfully!")

        # Check for required columns
        # if x_col not in data.columns or y_col not in data.columns:
        #     raise ValueError(f"Specified columns '{x_col}' or '{y_col}' not found in the CSV file.")
        
        plt.plot(data[x_col], data[y_col], color='blue')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title("Testing title")
        #plt.savefig("TestBarGraph.png")
        plt.show()

bar_graph("time.csv", 0,1)