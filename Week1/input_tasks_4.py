print("Please enter the number of lives.")
lives = int(input())
print("Please enter the energy level.")
energy = int(input())
print("Please enter the shield level.")
shield = int(input())

heart = "♥"
diamond = "♦"

print("\nHealth has been set.\n")
print(f"Lives:  {heart * lives}")
print(f"Energy: {diamond * energy}")
print(f"Shield: {diamond * shield}")
