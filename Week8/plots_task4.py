import matplotlib.pyplot as plt
import random

def data():
    path = {}
    path["line"] = input("Enter line style (:, --, -): ")
    path["color"] = input("Enter colour (r, g, b): ")
    path["marker"] = input("Enter marker style (o, s, ^): ")
    return path

def generate():
    amount = int(input("How many lines would you like to display? "))
    for _ in range(amount):
        values = data()
        x = random.sample(range(1, 20), 5)
        y = random.sample(range(1, 20), 5)
        plt.plot(x, y, f'{values["color"]}{values["marker"]}{values["line"]}')
    plt.title("PyPlot Dictionary Lines")
    plt.grid(True)
    plt.show()

def run_task4():
    print("Running....")
    generate()
    print("Done!")
