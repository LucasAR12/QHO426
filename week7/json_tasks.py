import json

def read(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        print(f"Place Name: {data['location']}")
        print(f"Population: {data['population']}")
        for bot in data["bots"]:
            name = bot["name"]
            strength = bot["stats"]["strength"]
            speed = bot["stats"]["speed"]
            print(f"{name} has a strength level of {strength} and a speed level of {speed}.")
    return data

def run():
    read("futurama.json")

def read_task2(file_path):
    print("Reading...", end="")
    with open(file_path, "r") as file:
        data = json.load(file)
    print("Done!")
    return data

def save(file_path, data):
    print("Exporting...", end="")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print("Done!")

def run_task2():
    json_data = read_task2("futurama.json")
    save("exported.json", json_data)

if __name__ == "__main__":
    run()