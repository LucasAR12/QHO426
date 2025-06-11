print("What level of brightness is required?")
level = int(input())

print("\nAdjusting brightness...\n")

for b in range(2, level + 1, 2):
    print("Brightness level: " + "*" * b)

print("\nComplete!")
