def removeOccurences(s, part):
    stack = []

    def checkMatch(stack, part):
        return "".join(stack[-len(part):]) == part

    for ch in s:
        stack.append(ch)

        if len(stack) >= len(part) and checkMatch(stack, part):
            for _ in range(len(part)):
                stack.pop()
    
    return "".join(stack)

print(removeOccurences("daabcbaabcbc", "abc"))

    

