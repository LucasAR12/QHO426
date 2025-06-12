import csv

# Activity 1
def read_csv(file_path):
    """Reads a CSV file and prints the headings and values."""
    with open(file_path, newline='') as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print("Headings:")
        print(headings)
        print("Values:")
        for values in csv_reader:
            print(values)

def run_task1():
    read_csv("clothing.csv")  # Caminho corrigido


# Activity 2
def extract(file_path):
    """Extracts and prints only the names of the items from the CSV."""
    print("Extracting...")
    names = ""
    with open(file_path, newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # ignore headings
        for values in csv_reader:
            names += values[1] + "\n"
    print("Done!")
    print("The extracted items are:")
    print(names, end="")

def run_task2():
    extract("clothing.csv")  # Caminho corrigido


# Activity 3
def export(file_path, num_items):
    """Exports user input data to the CSV file by appending."""
    print("Exporting...")
    with open(file_path, "a", newline='') as file:
        for _ in range(num_items):
            item_id = input("Please enter the item id:\n")
            item_name = input("Please enter the item name:\n")
            item_colour = input("Please enter the item colour:\n")
            line = f"{item_id},{item_name},{item_colour}\n"
            file.write(line)
    print("Done!")

def run_task3():
    while True:
        try:
            n = int(input("How many items do you want to export?\n"))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
    export("exported_items.csv", n)  # Caminho corrigido


# Menu principal
if __name__ == "__main__":
    print("Choose which task to run:")
    print("1 - Read CSV and display contents")
    print("2 - Extract names from CSV")
    print("3 - Export new items to CSV")
    choice = input("Enter 1, 2 or 3:\n").strip()

    if choice == "1":
        run_task1()
    elif choice == "2":
        run_task2()
    elif choice == "3":
        run_task3()
    else:
        print("Invalid choice. Exiting.")