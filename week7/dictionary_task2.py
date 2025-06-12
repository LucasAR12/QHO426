def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences

def display_keys(data):
    for key in data:
        print(key)

def display_values(data):
    for value in data.values():
        print(value)

def display_items(data):
    for key, value in data.items():
        print(f"{key}: {value}")

def run():
    data = pattern()
    print("Dictionary:")
    print(data)
    print("\nKeys:")
    display_keys(data)
    print("\nValues:")
    display_values(data)
    print("\nPairs:")
    display_items(data)

if __name__ == "__main__":
    run()
