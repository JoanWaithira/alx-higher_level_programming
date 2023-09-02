#!/usr/bin/python3
def text_indentation(text):
    """
    A function that prints a text with 2 new lines after eac character

    Args:
    text (str): The text in question

    Return: The printed text

    Raises:
    TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue

        sentence_endings = (".", "?", ":")
        sentence = ""
        for char in line:
            sentence += char
            if char in sentence_endings:
                print(sentence)
                print()
                sentence = ""
        if sentence:
            print(sentence)
