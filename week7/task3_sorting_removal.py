def observed_items():
    observations = []
    for _ in range(5):
        observations.append(input("Please enter an observation:\n"))
    return observations

def remove_observations(observations):
    while True:
        answer = input("Do you wish to remove an observation (yes/no)?\n").strip().lower()
        if answer == "yes":
            to_remove = input("What observation do you wish to remove?\n")
            if to_remove in observations:
                observations.remove(to_remove)
                print("Done!")
            else:
                print(f"Observation '{to_remove}' not found.")
        elif answer == "no":
            break

def run_task3():
    print("Counting observations...")
    observations = observed_items()
    remove_observations(observations)
    print("\nObservations:")
    unique_obs = sorted(set(observations))
    for obs in unique_obs:
        print(f"{obs} observed {observations.count(obs)} times.")

if __name__ == "__main__":
    run_task3()
