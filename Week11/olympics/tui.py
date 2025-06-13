def started(msg=""):
    print("-" * 85)
    print(f"Operation started: {msg}...\n")

def completed():
    print("\nOperation completed.")
    print("-" * 85)

def error(msg):
    print(f"Error! {msg}")

def menu():
    print("Please select one of the following options:")
    print(f"{'[years]':<10} List unique years")
    print(f"{'[tally]':<10} Tally up medals")
    print(f"{'[team]':<10} Tally up medals for each team")
    print(f"{'[exit]':<10} Exit the program\n")
    return input("Your selection: ").strip().lower()

def display_medal_tally(tally):
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")

def display_team_medal_tally(team_tally):
    for team, medals in team_tally.items():
        print(team)
        print(f"\tGold:{medals['Gold']}, Silver:{medals['Silver']}, Bronze:{medals['Bronze']}")

def display_years(years):
    for year in sorted(years, reverse=True):
        print(year)
