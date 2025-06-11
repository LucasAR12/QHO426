print("Program Started!")
print("Please enter an ASCII code:")

try:
    code = abs(int(input()))
    if code in range(32, 127):
        character = chr(code)
        print(f"The character represented by the ASCII code {code} is: {character}")
    else:
        print("Error: Please enter a value between 32 and 126 (inclusive).")
except ValueError:
    print("Error: Please enter a valid integer.")

print("Program Ended!")
