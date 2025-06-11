print("Program Started!")
print("Please enter a standard character:")

char = input()

if len(char) == 1:
    ascii_value = ord(char)
    print(f"The ASCII code for {char} is: {ascii_value}")
else:
    print("Error: Please enter only a single character.")

print("Program Ended!")
