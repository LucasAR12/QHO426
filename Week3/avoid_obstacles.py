print("How many obstacles should I avoid?")
num_obstacles = int(input())
avoided = 0
while avoided < num_obstacles:
    print("Avoiding...", end="")
    avoided += 1
    print(f"Done! {avoided} obstacles avoided.")
print("\nAll obstacles have been avoided.")
