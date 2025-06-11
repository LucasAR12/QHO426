def display_box(word):
    line = "*" * (len(word) + 4)
    print(line)
    print(f"* {word} *")
    print(line)

def display_lower(word):
    print(word.lower())

def display_upper(word):
    print(word.upper())

def display_mirrored(word):
    print(f"{word} | {word[::-1]}")

def repeat_word(word):
    print("How many times?")
    times = int(input())
    for i in range(times):
        if i % 2 == 0:
            print(word.upper())
        else:
            print(word.lower())

def run():
    print("Enter a word:")
    word = input()
    print("Choose an option:")
    print("1) Display in a Box")
    print("2) Display Lower-case")
    print("3) Display Upper-case")
    print("4) Display Mirrored")
    print("5) Repeat")
    choice = input()
    if choice == "1":
        display_box(word)
    elif choice == "2":
        display_lower(word)
    elif choice == "3":
        display_upper(word)
    elif choice == "4":
        display_mirrored(word)
    elif choice == "5":
        repeat_word(word)

run()
