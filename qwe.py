import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkOptionMenu
from rty import plot_line, plot_bar, plot_scatter, plot_histogram

class PlottingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CustomTkinter Matplotlib App")
        self.root.geometry("900x700")
        
        # Add a Matplotlib figure
        self.fig = Figure(figsize=(8, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(pady=10)
        
        # Input frame for x and y values
        self.input_frame = CTkFrame(self.root)
        self.input_frame.pack(fill="x", pady=10)

        CTkLabel(self.input_frame, text="x values (comma-separated):").pack(side="left", padx=10)
        self.entry_x = CTkEntry(self.input_frame, width=200)
        self.entry_x.pack(side="left", padx=10)

        CTkLabel(self.input_frame, text="y values (comma-separated):").pack(side="left", padx=10)
        self.entry_y = CTkEntry(self.input_frame, width=200)
        self.entry_y.pack(side="left", padx=10)

        # Message label
        self.label_message = CTkLabel(self.root, text="")
        self.label_message.pack(pady=5)

        # Dropdown menu to choose plot type
        self.plot_menu = CTkOptionMenu(self.root, values=["Line Plot", "Bar Plot", "Scatter Plot", "Histogram"])
        self.plot_menu.pack(pady=20)
        
        # Plot button
        self.plot_button = CTkButton(self.root, text="Plot", command=self.choose_plot)
        self.plot_button.pack(pady=10)
    
    def update_canvas(self):
        """Clear the existing canvas widget and update it with the new plot."""
        self.canvas.get_tk_widget().pack_forget()
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=10)
    
    def choose_plot(self):
        """Select the plotting function based on user choice."""
        selected_plot = self.plot_menu.get()

        if selected_plot == "Line Plot":
            plot_line(self.fig, self.entry_x, self.entry_y, self.label_message, self.update_canvas)
        elif selected_plot == "Bar Plot":
            plot_bar(self.fig, self.entry_x, self.entry_y, self.label_message, self.update_canvas)
        elif selected_plot == "Scatter Plot":
            plot_scatter(self.fig, self.update_canvas)
        elif selected_plot == "Histogram":
            plot_histogram(self.fig, self.update_canvas)
        else:
            print("Invalid plot type selected")

# Run the application
if __name__ == "__main__":
    root = CTk()
    app = PlottingApp(root)
    root.mainloop()
