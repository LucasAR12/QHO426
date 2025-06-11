choice = input("Choose your adventure type (scary/safe/short/long):\n")

if choice == "scary" or choice == "short":
    print("Entering the dark forest!")
    hear = input("What did I hear?\n")
    see = input("What did I see?\n")
    if hear == "grrr" and see == "two red eyes":
        print("There is a scary creature. I should get out of here!")
    else:
        print("I am a little scared but I will continue.")
elif choice == "safe" or choice == "long":
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")
