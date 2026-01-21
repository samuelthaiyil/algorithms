def removeDuplicates(s):
    stack = []

    for i in s:
        if not stack or i != stack[len(stack) - 1]:
            stack.append(i)
        else:
            stack.pop()
    
    return "".join(stack)

print(removeDuplicates("abbbabaaa"))

