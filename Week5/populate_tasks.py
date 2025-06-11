def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def menu_and_input():
    steps = directions()
    for index in range(len(steps)):
        print(f"{index}: {steps[index]}")
    choice = int(input())
    return steps[choice]

def run_task4():
    route = []
    print("Working out escape route...\n")
    for _ in range(5):
        print()
        direction = menu_and_input()
        route.append(direction)
    print(f"\nEscape route: {route}")

if __name__ == "__main__":
    run_task4()
