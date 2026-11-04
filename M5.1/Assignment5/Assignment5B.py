# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 5

import random

def create_map(rows, cols):
    """Build the treasure map (nested list) and count the treasures."""
    treasure_map = []
    total_treasures = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            num = random.randint(0, 100)
            if num < 30:
                row.append("T")
                total_treasures += 1
            elif num < 50:
                row.append("X")
            else:
                row.append("E")
        treasure_map.append(row)
    return treasure_map, total_treasures


def display_map(treasure_map):
    """Print the map using nested loops."""
    for i in range(len(treasure_map)):
        line = ""
        for j in range(len(treasure_map[i])):
            line += treasure_map[i][j]
            if j < len(treasure_map[i]) - 1:
                line += " "
        print(line)


def end_game(treasure_map, score, traps, explored):
    print("Congratulations! All treasures have been collected!")
    print("Final Map:")
    display_map(treasure_map)
    print("Final Score =", score)
    print("Traps Encountered =", traps)
    print("Locations explored =", explored)


def main():
    rows = int(input("Enter rows : "))
    cols = int(input("Enter Columns : "))

    treasure_map, remaining = create_map(rows, cols)
    print("Total Treasures :", remaining)
    display_map(treasure_map)

    score = 0
    streak = 0
    traps = 0
    explored = 0

    # If there are no treasures, the game ends immediately
    if remaining == 0:
        end_game(treasure_map, score, traps, explored)
        return

    while remaining > 0:
        row = int(input("Enter row (0 to " + str(rows - 1) + ") : "))
        col = int(input("Enter column (0 to " + str(cols - 1) + ") : "))
        location = (row, col)  # selected location stored as a tuple

        cell = treasure_map[location[0]][location[1]]

        if cell == "T":
            streak += 1
            if streak >= 2:
                score += 15
                print("Treasure found! +15 points (including bonus).")
            else:
                score += 10
                print("Treasure found! +10 points.")
            remaining -= 1
            explored += 1
            treasure_map[location[0]][location[1]] = "V"
        elif cell == "X":
            score -= 5
            traps += 1
            explored += 1
            streak = 0
            treasure_map[location[0]][location[1]] = "V"
            print("You hit a trap! -5 points.")
        elif cell == "E":
            explored += 1
            streak = 0
            treasure_map[location[0]][location[1]] = "V"
            print("Nothing found at this location.")
        else:  # already visited, streak unaffected
            print("You have already explored this location.")

        display_map(treasure_map)
        print("Current score =", score)
        print("Remaining Treasures =", remaining)

    end_game(treasure_map, score, traps, explored)

main()