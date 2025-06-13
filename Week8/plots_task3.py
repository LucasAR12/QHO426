import matplotlib.pyplot as plt

def coordinate():
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    return (x, y)

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for _ in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]

def run_task3():
    values = path()
    plt.plot(values[0], values[1], 'ro--')
    plt.title("PyPlot Path")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    plt.show()
