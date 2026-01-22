def validParentheses(s):
    stack = []
    mappings = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for ch in s:
        if ch not in mappings:
            stack.append(ch)
        else:
            if not stack or stack.pop() != mappings[ch]:
                return False
    
    return not stack
