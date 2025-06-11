print("How many bars should be charged?")
num_bars = int(input())
charged = 0
while charged < num_bars:
    charged += 1
    print("Charging:", "█ " * charged)
print("\nThe battery is fully charged.")
