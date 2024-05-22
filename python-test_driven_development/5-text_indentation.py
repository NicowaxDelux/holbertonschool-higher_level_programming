#!/usr/bin/python3
"""text indentation"""


def text_indentation(text):
    """ text indentation

    arg:
    text(str):text string

    Raise
    TypeError: when text is not str

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    phrase = ""
    i = 0
    while i < len(text):
        if text[i] != "." and text[i] != "?" and text[i] != ":":
            phrase += text[i]
        else:
            phrase += text[i]
            print(phrase)
            print()
            phrase = ""
            while i < (len(text) - 1) and text[i+1] == " ":
                i += 1
        i += 1
    print(phrase, end="")
