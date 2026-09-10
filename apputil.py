def palindrome(word):
    """Check whether a word or phrase is a palindrome.

    Ignores case, spaces, and punctuation.

    Args:
        word (str): The word or phrase to check.

    Returns:
        bool: True if the input is a palindrome, False otherwise.
    """
    cleaned = ""
    for char in word.lower():
        if char.isalnum():
            cleaned += char

    return cleaned == cleaned[::-1]


def parentheses(sequence):
    """Check whether parentheses in a string are balanced.

    Uses a stack: each '(' is pushed, and each ')' must pop
    a matching '(' off the stack.

    Args:
        sequence (str): The string to check.

    Returns:
        bool: True if parentheses are balanced, False otherwise.
    """
    stack = []
    for char in sequence:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

