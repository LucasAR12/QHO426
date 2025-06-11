print("What phrase do you want to see in reverse?")
phrase = input()

print("\nReversing...\n")

reversed_phrase = ""
for i in range(len(phrase) - 1, -1, -1):
    reversed_phrase += phrase[i]

print("The phrase is:", reversed_phrase)
