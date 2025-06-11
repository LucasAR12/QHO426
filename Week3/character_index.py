print("What word do you see?")
user_word = input()

print("\nDisplaying index positions...\n")

for i in range(len(user_word)):
    print(f"index {i}: {user_word[i]}")

print("\nDone!")
