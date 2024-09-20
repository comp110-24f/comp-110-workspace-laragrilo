"""EX02 - Chardle Excercise"""

__author__ = "730602202"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    word_variable = input("Enter a 5-character word: ")
    # I was struggling to get the input to promppt user to input word
    # The run tab in the trailhead doesn't show my message to input a word
    # Realized i had to call the function so it would work

    if len(word_variable) == 5:
        return word_variable
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    letter_variable = input("Enter a single character: ")
    if len(letter_variable) == 1:
        return letter_variable
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    count: int = 0
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)
    return None


# My function is running a little weird, its repeating input_word and input_letter
# And adter it prompt those twice it runs contains_char, not sure what's the issue

main()

if __name__ == "__main__":
    main()
