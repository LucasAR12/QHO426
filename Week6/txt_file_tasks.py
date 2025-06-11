import os

# Activity 1
def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)

def run():
    print("Processing...")
    cwd()

# Activity 2
def display_chars(file_path, num_chars):
    with open(file_path, "r") as file:
        data = file.read(num_chars)
        print(f"The first {num_chars} characters are:")
        print(data)
        print()

def display_line(file_path):
    with open(file_path, "r") as file:
        line = file.readline().strip()
        print("The first line is:")
        print(line)
        print()

def display_text(file_path):
    with open(file_path, "r") as file:
        text = file.read()
        print("The full text is:")
        print(text)
        print()

def run_task2():
    file_path = "library.txt"
    display_chars(file_path, 5)
    display_line(file_path)
    display_text(file_path)

# Activity 3
def search(file_name):
    print("Searching...")
    with open(file_name, "r") as file:
        for line in file:
            # strip() to avoid trailing newline messing with the message
            location = line.strip()
            print(f"Looked in {location}.")
    print("...Done!")

def run_task3():
    search("library.txt")

# Activity 4
def search_books(file_path):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("Section"):
                sections += line
            else:
                books += line
    print("Done!")
    return f"{sections}\n\n{books}"

def save(file_path, data):
    print("Saving...")
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")

def run_task4():
    data = search_books("books.txt")
    save("section-books.txt", data)


# Run Activity 2 if executed directly
if __name__ == "__main__":
    run_task2()
