even_count = 0
odd_count = 0
for i in range(1, 4):
    n = int(input(f"Please enter the {['first','second','third'][i-1]} whole number.\n"))
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"There were {even_count} even and {odd_count} odd numbers.")
