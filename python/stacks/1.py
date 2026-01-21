def validParentheses(s):
    mappings = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = []

    for char in s:
        if char not in mappings:
            stack.append(char)
        elif not stack or mappings[char] != stack.pop():
            return False

    return not stack

validParentheses("()")
