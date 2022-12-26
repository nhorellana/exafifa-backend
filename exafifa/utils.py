from exafifa.spreadsheet import spreadsheets_operations
from collections import defaultdict


def update_positions(results):
    spreadsheets_operations("delete", "Liga!A1:G1000")
    # [["Nicolas","Antonio","1","2"],["Nicolas","Antonio","2","2"],["Nicolas","Antonio","4","2"],["Nicolas","Antonio","5","2"],["Nicolas","Antonio","5","5"],["Nicolas","Antonio","3","5"]]
    # content = {"record": [], "goal_difference": 0}
    # TODO: add goal difference
    ligue = defaultdict(list)
    for game in results:
        result_1, result_2 = ("", "")  # w, l, t
        player_1, player_2, goals_1, goals_2 = game
        if goals_1 == goals_2:
            result_1 = "t"
            result_2 = "t"
        elif int(goals_1) > int(goals_2):
            result_1 = "w"
            result_2 = "l"
        else:
            result_1 = "l"
            result_2 = "w"
        ligue[player_1].append(result_1)
        ligue[player_2].append(result_2)
    table = [["Position", "Name", "Wins", "Ties", "Loses", "Played", "Points"]]
    positions = calculate_points(ligue)
    print(f"Posiciones {positions}")
    table.extend(positions)
    return table


def calculate_points(ligue):
    table = []
    for player, results in ligue.items():
        points = 0
        wins = results.count("w")
        ties = results.count("t")
        loses = results.count("l")
        points += 3 * wins
        points += ties
        played = wins + ties + loses
        table.append([player, wins, ties, loses, played, points])
    sorted_positions = sorted(table, key=lambda x: x[-1], reverse=True)
    for i, inner_list in enumerate(sorted_positions):
        inner_list.insert(0, i + 1)
    return sorted_positions
