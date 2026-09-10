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

# add code below ...
