def applyOps(ops):
    stack = []
    sum = 0

    for o in ops:
        if o.startswith("-") or o.isdigit():
            stack.append(int(o))
        elif o == "+":
            val1 = stack[-1] if stack[-1] is not None else 0
            val2 = stack[-2] if stack[-2] is not None else 0

            stack.append((int(val1) + int(val2)))
        elif o == "D":
            val1 = stack[-1] if stack[-1] is not None else 0
            
            stack.append((int(val1) * 2))
        elif o == "C":
            stack.pop()
    
    for el in stack:
        sum += int(el)
    
    return sum

print(applyOps(["1", "C"]))
            