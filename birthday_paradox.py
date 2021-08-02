"""
Birthday Problem, is the surprisingly high probability that two people will have the
same birthday even in a small group of people. In a group of 70 people, there’s a 99.9 percent chance
of two people having a matching birthday. But even in a group as small as 23 people, there’s a 50 percent
chance of a matching birthday. This program performs several probability experiments to determine
the percentages for groups of different sizes.
"""

from datetime import date, timedelta
import random


def main():
    """"""
    print("How many birthdays shall I generate?(Max 100)")
    num_people = ""
    # Keep asking until the user enters a valid amount.
    while not (num_people.isdecimal() and (0 < int(num_people) <= 100)):
        num_people = input(">")

    dates = generate_dates(int(num_people))
    print(f"Here are {num_people} birthdays:")
    for i in range(int(num_people)):
        print(dates[i].strftime("%d %b"), end=", ")

    # Determine if there are birthdays that match.
    duplicates = find_duplicate_dates(dates)
    if len(duplicates) > 0:
        print("\nIn this simulation, multiple people have a birthday on:")
        print([d.strftime("%d %b") for d in duplicates])
    else:
        print("\nIn this simulation, there is no matching birthdays.")

    # Run through 100,000 simulations:
    print(f"Generating {num_people} random birtdays 100,000 times...")
    match_simulations = 0
    for i in range(100000):
        if i % 10_000 == 0:
            print(i, "simulations run...")
        dates = generate_dates(int(num_people))
        if find_duplicate_dates(dates) != []:
            match_simulations += 1
    print("100000 simultations run.")

    # Display simulation results:
    probability = round(match_simulations / 100000 * 100, 2)
    print(
        f"{num_people} people have {probability}% chance of having matching at least 1 birthday in their group."
    )


def find_duplicate_dates(dates):
    """Returns a duplicate date from the list of dates, if it exists."""
    # Check if duplicates exist in the list.
    if len(dates) == len(set(dates)):
        return []  # all dates are unique

    # Compare each date to every other date
    matching_dates = []
    for i, date in enumerate(dates):
        for j, date_compare in enumerate(dates[i + 1 :]):
            if date == date_compare:
                matching_dates.append(date)
    return matching_dates


def generate_dates(num_of_dates):
    """Generate and retuens a list of number random dates."""
    dates = []
    for i in range(num_of_dates):
        # The year is unimportant
        start_of_year = date(2021, 1, 1)
        # Get random day in the year
        day = random.randint(0, 364)
        new_date = start_of_year + timedelta(days=day)
        dates.append(new_date)
    return dates


def generate_dates_1(num_of_dates):
    """Another option. Generate and retuens a list of number random dates."""
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dates = []
    for i in range(num_of_dates):
        new_month = random.randint(1, 12)
        new_day = random.randint(1, days_in_month[new_month - 1])
        new_date = date(year=2021, month=new_month, day=new_day)
        dates.append(new_date)
    return dates


if __name__ == "__main__":
    main()
