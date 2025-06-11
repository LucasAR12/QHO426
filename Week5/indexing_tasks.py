def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run_task2():
    print("Moving...")
    path = movements()
    for i in range(0, len(path), 2):
        print(f"{path[i]} for {path[i+1]} steps")

if __name__ == "__main__":
    run_task2()
