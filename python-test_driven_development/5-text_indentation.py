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
    
    words = 0
    while words < len(text):
        if text[words] in [':', '.', '?']:
            print(text[words])
            print()
            words += 1
        else:
            print(text[words], end='')
        words += 1
