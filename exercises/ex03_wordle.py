"""Exercise 03 - Wordle"""

__author__ = "730602202"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    number_of_turns: int = 1
    while number_of_turns <= 6:
        print(f"=== Turn {number_of_turns}/6 ===")
        word_input = input_guess(len(secret))
        print(emojified(word_input, secret))
        if word_input == secret:
            print(f"You won in {number_of_turns}/6 turns!")
            return
        number_of_turns += 1
    print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Word input has to equal length of secret word"""
    word_input = input(f"Enter a {secret_word_len} character word: ")
    while len(word_input) != secret_word_len:
        word_input = input(f"That wasn't {secret_word_len} chars! Try again:")
    return word_input


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Finding a character match"""
    assert len(char_guess) == 1
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    return False


# I'm getting issues importing the contains_char in the REPL, this was happening w/ CQ4
# Solved it the same way I did for CQ4, i exited and came back in and it worked


def emojified(guess: str, secret: str) -> str:
    # I'm having a hard time thinking how to make the yellow boxes match the characters
    # i figured logically how to do this with an elif statement

    """Checking for matches using emojis"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emojis: str = ""
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            emojis += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        idx += 1
    return emojis


if __name__ == "__main__":
    main(secret="codes")
