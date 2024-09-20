"""CQ00 First Challenge Question"""

__author__ = "730602202"


def mimic(message: str) -> str:
    """Repeating Messages Back to Me"""
    return message


def main() -> None:
    """print reuslt of mimic function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
