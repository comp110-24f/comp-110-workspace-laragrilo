"""Tea Party Planner"""

__author__: str = "730602202"


def main_planner(guests: int) -> None:
    """Bring all functions together and print out total output"""
    print("A Cozy Tea Party for " + str(guests) + " People" + "!")
    print("Tea bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# In step 4, I faced issues getting the code to run and encountered syntax errors.
# I fixed some of them, the costs function still wouldn’t print correctly.
# I ran into some errors on Gradescope and attended office hours for assistance.
# During office hours, I realized that I was incorrectly inputting the parameters
# Tried to call tea_count, which had not yet been defined, causing the function to fail


def tea_bags(people: int) -> int:
    """Calculating the number of teabags based on how many people attend"""
    return 2 * people


def treats(people: int) -> int:
    """Calculating the number of treats people need based on tea bags"""
    return int(tea_bags(people=people) * 1.5)


# I wasn't being able to run the treats function
# I though it was because I labeled the type wrong
# Realized I needed to input the tea_bags with argument people=people to make it work


def cost(tea_count: int, treat_count: int) -> float:
    """Computing the cost of the tea bags and treats combined"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
