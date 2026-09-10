def parentheses(sequence):
    """Check whether parentheses in a string are balanced.

    Non-parenthesis characters are ignored.

    Args:
        sequence (str): The string to check.

    Returns:
        bool: True if parentheses are balanced, False otherwise.
    """
    balance = 0
    for char in sequence:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1

        if balance < 0:
            return False

    return balance == 0

if __name__ == "__main__":
    print(palindrome("racecar"))              # Expected: True
    print(palindrome("Nurses Run"))            # Expected: True
    print(palindrome("Sit on a potato pan, Otis."))  # Expected: True
    print(palindrome("hello"))                 # Expected: False

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
if __name__ == "__main__":
    assert parentheses("((blah)()()())") is True
    assert parentheses("(((())blee))") is True
    assert parentheses("(()hello((())()))") is True
    assert parentheses("((((((())") is False
    assert parentheses("()))") is False
    print("All parentheses tests passed!")
