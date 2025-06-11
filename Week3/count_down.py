print("How far are we from the target?")
steps = int(input())

for step in range(steps, 0, -1):
    print(f"{step} steps remaining")

print("\nTarget achieved!")
