def observed_items():
    observations = []
    for _ in range(7):
        observations.append(input("Please enter an observation:\n"))
    return observations

def run_task2():
    print("Counting observations...")
    observations = observed_items()
    observation_set = set()
    for item in observations:
        observation_set.add((item, observations.count(item)))
    for obs, cnt in observation_set:
        print(f"{obs} observed {cnt} times.")

if __name__ == "__main__":
    run_task2()
