print("Please enter a sequence")
sequence = input()

print("\nPlease enter the character for the marker")
marker = input()

start = -1
end = -1

for i in range(len(sequence)):
    if sequence[i] == marker:
        if start == -1:
            start = i
        else:
            end = i
            break

distance = end - start - 1
print(f"\nThe distance between the markers is {max(distance, 0)}.")
