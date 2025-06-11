print("How many numbers should I sum up?")
count = int(input())
total = 0
current = 1
while current <= count:
    print(f"Please enter number {current} of {count}:")
    num = int(input())
    total += num
    current += 1
print(f"\nThe answer is {total}.")
