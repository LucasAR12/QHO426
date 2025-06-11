print("How many rows should I have?")
rows = int(input())

print("\nHow many columns should I have?")
columns = int(input())

print("\nHere I go:\n")

for _ in range(rows):
    for _ in range(columns):
        print(":-)", end=" ")
    print()

print("\nDone!")
