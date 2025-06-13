from plots_task1 import run_task1
from plots_task2 import run_task2
from plots_task3 import run_task3
from plots_task4 import run_task4

def menu():
    print("WEEK 8 MENU")
    print("1. Task 1: Simple Line Plot")
    print("2. Task 2: Squares Plot")
    print("3. Task 3: User Input Path")
    print("4. Task 4: Dictionary + Random Plot")
    print("0. Exit")

def main():
    while True:
        menu()
        option = input("Choose an option: ")
        if option == "1":
            run_task1()
        elif option == "2":
            run_task2()
        elif option == "3":
            run_task3()
        elif option == "4":
            run_task4()
        elif option == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
