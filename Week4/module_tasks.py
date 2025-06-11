import random

def play_guess_the_number():
    print("Please enter the minimum value:")
    min_val = int(input())
    print("Please enter the maximum value:")
    max_val = int(input())
    target = random.randint(min_val, max_val)
    print(f"I am thinking of a number between {min_val} and {max_val}. Can you guess what it is?")
    while True:
        guess = int(input())
        if guess < target:
            print("Your guess is too low.")
            print("Try again:")
        elif guess > target:
            print("Your guess is too high.")
            print("Try again:")
        else:
            print("Congratulations! You guessed my number!")
            break

# play_guess_the_number()
