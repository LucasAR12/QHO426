cover = input("What type of cover does the book have?\n")
if cover == "soft":
    perfect_bound = input("Is the book perfect-bound?\n")
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")
