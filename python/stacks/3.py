def removeStars(s):
    stack = []

    for i in s:
        if (not stack and i != "*") or i != "*":
            stack.append(i)
        else:
            stack.pop()
    
    return "".join(stack)

print(removeStars("u*ensso****x*q"))