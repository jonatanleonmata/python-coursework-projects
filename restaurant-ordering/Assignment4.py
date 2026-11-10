# Class: CSE 1321L
# Section: BW2
# Term: Fall 2026
# Instructor: Hunter Osborne
# Name: Jonatan Leon Mata
# Assignment: 4


def input_choice(lowest_option, highest_option):
    choice = int(input("> "))

    # Keep asking until the menu choice is in range.
    while choice < lowest_option or choice > highest_option:
        print("Please, enter an option between " + str(lowest_option) + " and " + str(highest_option))
        choice = int(input("> "))

    return choice


def input_money():
    amount = float(input("> $"))

    while amount < 0:
        print("Please, enter a valid monetary amount.")
        amount = float(input("> $"))

    return amount


def burgers():
    amount = 0.0

    while True:
        print("1. Big Owl Burger - Single ($5.99)")
        print("2. Big Owl Burger - Double ($7.99)")
        print("3. Return")
        choice = input_choice(1, 3)

        if choice == 1:
            print("1 Big Owl Burger - Single added")
            amount += 5.99
            print()
        elif choice == 2:
            print("1 Big Owl Burger - Double added")
            amount += 7.99
            print()
        else:
            print()
            return amount


def sides():
    amount = 0.0

    while True:
        print("1. Fries ($3.49)")
        print("2. Onion Rings ($2.99)")
        print("3. Get Back")
        choice = input_choice(1, 3)

        if choice == 1:
            print("1 Fries added")
            amount += 3.49
            print()
        elif choice == 2:
            print("1 Onion Rings added")
            amount += 2.99
            print()
        else:
            print()
            return amount


def drinks():
    amount = 0.0

    while True:
        print("1. Scrappy-Cola - Small ($2.49)")
        print("2. Scrappy-Cola - Medium ($2.79)")
        print("3. Scrappy-Cola - Large ($2.99)")
        print("4. Dr Owl - Small ($2.49)")
        print("5. Dr Owl - Medium ($2.79)")
        print("6. Dr Owl - Large ($2.99)")
        print("7. Get Back")
        choice = input_choice(1, 7)

        if choice == 1:
            print("1 Scrappy-Cola - Small added")
            amount += 2.49
        elif choice == 2:
            print("1 Scrappy-Cola - Medium added")
            amount += 2.79
        elif choice == 3:
            print("1 Scrappy-Cola - Large added")
            amount += 2.99
        elif choice == 4:
            print("1 Dr. Owl - Small added")
            amount += 2.49
        elif choice == 5:
            print("1 Dr. Owl - Medium added")
            amount += 2.79
        elif choice == 6:
            print("1 Dr. Owl - Large added")
            amount += 2.99
        else:
            print()
            return amount

        print()


def order():
    subtotal = 0.0

    while True:
        print("Choose an option: ")
        print("1. Burgers")
        print("2. Sides")
        print("3. Drinks")
        print("4. Check out")
        choice = input_choice(1, 4)
        print()

        if choice == 1:
            subtotal += burgers()
        elif choice == 2:
            subtotal += sides()
        elif choice == 3:
            subtotal += drinks()
        else:
            return subtotal


def calculate_tip(subtotal):
    print("Choose a tip option:")
    print("1. $" + format(subtotal * 0.18, ".2f") + " (18%)")
    print("2. $" + format(subtotal * 0.20, ".2f") + " (20%)")
    print("3. $" + format(subtotal * 0.25, ".2f") + " (25%)")
    print("4. Custom")
    print("5. No Tip")
    choice = input_choice(1, 5)

    if choice == 1:
        return subtotal * 0.18
    elif choice == 2:
        return subtotal * 0.20
    elif choice == 3:
        return subtotal * 0.25
    elif choice == 4:
        print("Custom tip:")
        return input_money()
    else:
        return 0.0


def calculate_tax(subtotal):
    return subtotal * 0.06


def print_total(subtotal, tip, tax):
    # Format all money values with two decimal places.
    total = subtotal + tip + tax
    print("Subtotal: $" + format(subtotal, ".2f"))
    print("Tip: $" + format(tip, ".2f"))
    print("Tax: $" + format(tax, ".2f"))
    print("Total: $" + format(total, ".2f"))


subtotal = order()
tip = calculate_tip(subtotal)
tax = calculate_tax(subtotal)
print()
print_total(subtotal, tip, tax)
