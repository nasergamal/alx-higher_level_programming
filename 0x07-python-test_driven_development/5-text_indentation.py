#!/usr/bin/python3
'''text_indentation function'''


def text_indentation(text):
    '''print text without extra space and print newline after delmiters
    Args:
        text (str): the string that will be printed
    Raise:
        TypeError: if text is not string
    '''
    if not text or not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == " ":
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:" or text[i] == '\n':
            print("\n") if text[i] != '\n' else ""
            if i + 1 < len(text):
                while i + 1 < len(text) and text[i + 1] == " ":
                    i += 1
        i += 1
