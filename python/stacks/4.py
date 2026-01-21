def minAddToMakeValid(s):
    stack = []
    moves = 0

    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                moves += 1

    return moves + len(stack)

print(minAddToMakeValid(""))
        
