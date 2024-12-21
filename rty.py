import numpy as np

def plot_line(fig, entry_x, entry_y, label_message, update_canvas):
    """Create a line plot."""
    fig.clear()
    ax = fig.add_subplot(111)
    try:
        x = list(map(float, entry_x.get().split(',')))
        y = list(map(float, entry_y.get().split(',')))

        if len(x) != len(y):
            label_message.configure(text="Error: x and y must have the same length!", text_color="red")
            return

        ax.plot(x, y, label="Line Plot", color="blue")
        ax.set_title("Line Plot")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend()
        label_message.configure(text="Line Plot updated successfully!", text_color="green")
        update_canvas()
    except ValueError:
        label_message.configure(text="Error: Please enter valid numeric values separated by commas.", text_color="red")

def plot_bar(fig, entry_x, entry_y, label_message, update_canvas):
    """Create a bar plot."""
    fig.clear()
    ax = fig.add_subplot(111)
    try:
        x = list(map(float, entry_x.get().split(',')))
        y = list(map(float, entry_y.get().split(',')))

        if len(x) != len(y):
            label_message.configure(text="Error: x and y must have the same length!", text_color="red")
            return

        ax.bar(x, y, label="Bar Plot", color="orange")
        ax.set_title("Bar Plot")
        ax.set_xlabel("Category")
        ax.set_ylabel("Value")
        ax.legend()
        update_canvas()
    except ValueError:
        label_message.configure(text="Error: Please enter valid numeric values separated by commas.", text_color="red")

def plot_scatter(fig, update_canvas):
    """Create a scatter plot."""
    fig.clear()
    ax = fig.add_subplot(111)
    
    x = np.random.rand(50)
    y = np.random.rand(50)
    
    ax.scatter(x, y, label="Scatter Plot", color="green")
    ax.set_title("Scatter Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()
    update_canvas()

def plot_histogram(fig, update_canvas):
    """Create a histogram plot."""
    fig.clear()
    ax = fig.add_subplot(111)
    
    data = np.random.randn(1000)
    
    ax.hist(data, bins=20, label="Histogram", color="purple", alpha=0.7)
    ax.set_title("Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.legend()
    update_canvas()
