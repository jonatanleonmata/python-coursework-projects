# Class: CSE 1321L
# Section: BW2
# Term: Fall 2026
# Instructor: Hunter Osborne
# Name: Jonatan Leon Mata
# Assignment: 5B

import random


def display_map(treasure_map):
    for row in treasure_map:
        for column in range(len(row)):
            print(row[column], end="")
            if column < len(row) - 1:
                print(" ", end="")
        print()


def main():
    rows = int(input("Enter rows : "))
    columns = int(input("Enter Columns : "))

    treasure_map = []
    total_treasures = 0

    # Build each row of the map one location at a time.
    for row_index in range(rows):
        map_row = []
        for column_index in range(columns):
            random_number = random.randint(0, 100)
            if random_number < 30:
                map_row.append("T")
                total_treasures = total_treasures + 1
            elif random_number < 50:
                map_row.append("X")
            else:
                map_row.append("E")
        treasure_map.append(map_row)

    remaining_treasures = total_treasures
    score = 0
    traps_encountered = 0
    locations_explored = 0
    treasure_streak = 0

    print("Total Treasures : " + str(total_treasures))
    display_map(treasure_map)

    while remaining_treasures > 0:
        selected_row = int(input("Enter row (0 to " + str(rows - 1) + ") : "))
        selected_column = int(input("Enter column (0 to " + str(columns - 1) + ") : "))
        selected_location = (selected_row, selected_column)
        location = treasure_map[selected_location[0]][selected_location[1]]

        if location == "T":
            if treasure_streak > 0:
                score = score + 15
                print("Treasure found! +15 points (including bonus).")
            else:
                score = score + 10
                print("Treasure found! +10 points.")
            treasure_streak = treasure_streak + 1
            remaining_treasures = remaining_treasures - 1
            locations_explored = locations_explored + 1
            treasure_map[selected_location[0]][selected_location[1]] = "V"
        elif location == "X":
            score = score - 5
            traps_encountered = traps_encountered + 1
            locations_explored = locations_explored + 1
            treasure_streak = 0
            treasure_map[selected_location[0]][selected_location[1]] = "V"
            print("You hit a trap! -5 points.")
        elif location == "E":
            locations_explored = locations_explored + 1
            treasure_streak = 0
            treasure_map[selected_location[0]][selected_location[1]] = "V"
            print("Nothing found at this location.")
        else:
            print("You have already explored this location.")

        display_map(treasure_map)
        print("Current score = " + str(score))
        print("Remaining Treasures = " + str(remaining_treasures))

    print("Congratulations! All treasures have been collected!")
    print("Final Map:")
    display_map(treasure_map)
    print("Final Score = " + str(score))
    print("Traps Encountered = " + str(traps_encountered))
    print("Locations explored = " + str(locations_explored))


main()
