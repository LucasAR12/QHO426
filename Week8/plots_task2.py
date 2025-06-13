import matplotlib.pyplot as plt

def small():
    x = [1, 1, 2, 2, 1]
    y = [1, 2, 2, 1, 1]
    plt.plot(x, y, 'ro:', label="Small")

def medium():
    x = [0, 0, 3, 3, 0]
    y = [0, 3, 3, 0, 0]
    plt.plot(x, y, 'gs--', label="Medium")

def large():
    x = [-1, -1, 4, 4, -1]
    y = [-1, 4, 4, -1, -1]
    plt.plot(x, y, 'bp-', label="Large")

def run_task2():
    small()
    medium()
    large()
    plt.title("PyPlot Squares")
    plt.grid(True)
    plt.legend()
    plt.show()
