import tui

def list_years(data):
    tui.started("Listing years...")
    years = set()
    for record in data:
        if len(record) >= 10:
            years.add(int(record[9]))  # Coluna 'Year'
    tui.display_years(years)
    tui.completed()

def tally_medals(data):
    tui.started("Tallying medals...")
    tally = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for record in data:
        if len(record) >= 15:
            medal = record[14]
            if medal in tally:
                tally[medal] += 1
    tui.display_medal_tally(tally)
    tui.completed()

def tally_team_medals(data):
    tui.started("Tallying medals for each team...")
    team_tally = {}

    for record in data:
        if len(record) < 15:
            continue

        team = record[6]
        medal = record[14]

        if medal in ("Gold", "Silver", "Bronze"):
            if team not in team_tally:
                team_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            team_tally[team][medal] += 1

    tui.display_team_medal_tally(team_tally)
    tui.completed()
