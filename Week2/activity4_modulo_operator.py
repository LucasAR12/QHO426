first_num = int(input("Please enter the first number.\n"))
second_num = int(input("Please enter the second number.\n"))
if first_num < second_num:
    print("The first number is the smallest!")
elif second_num < first_num:
    print("The second number is the smallest!")
else:
    print("Both are equal!")
