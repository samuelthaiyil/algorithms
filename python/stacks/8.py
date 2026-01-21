def scoreOfParentheses(s):
    stack = [0]

    for ch in s:
        if ch == "(":
            # increase depth
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2 * v, 1)
    
    return stack.pop()
 
print(scoreOfParentheses("(()(()))"))
print(scoreOfParentheses("()()()()"))     
        