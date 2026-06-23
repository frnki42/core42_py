import sys
import string


def text_analyzer(text=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if text is None:
        text = input("What is the text to analyze?\n")
    assert isinstance(text, str), "argument is not a string"
    count_upper = 0
    count_lower = 0
    count_spaces = 0
    count_punctuation = 0
    for character in text:
        if character.isupper():
            count_upper += 1
        elif character.islower():
            count_lower += 1
        elif character.isspace():
            count_spaces += 1
        elif character in string.punctuation:
            count_punctuation += 1
    print(f"The text contains {len(text)} printable character(s):")
    print(f"- {count_upper} upper letter(s)")
    print(f"- {count_lower} lower letter(s)")
    print(f"- {count_punctuation} punctuation mark(s)")
    print(f"- {count_spaces} space(s)")


if __name__ == "__main__":
    assert len(sys.argv) < 3, "more than one argument is provided"
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
