"""Guessing a Number"""

__author__ = "730602202"


def guess_a_number() -> None:
    secret: int = 7
    guess: int = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low!" + " The secret number is 7")
    else:
        print("Your guess was too high!" + " The secret number is 7")
    return None


if __name__ == "__main__":
    guess_a_number()
