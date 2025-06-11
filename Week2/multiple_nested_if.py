location = input("Where should I look?\n")

if location == "in the bedroom":
    place = input("Where in the bedroom should I look?\n")
    if place == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")
elif location == "in the bathroom":
    place = input("Where in the bathroom should I look?\n")
    if place == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")
elif location == "in the living room":
    place = input("Where in the living room should I look?\n")
    if place == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")
else:
    print("I do not know where that is but I will keep looking.")
