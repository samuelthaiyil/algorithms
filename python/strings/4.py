def backspaceCompare(s: str, t: str):
    def build(S):
        ans = []
        for i in S:
            if i != '#':
                ans.append(i)
            elif ans:
                ans.pop()

        return "".join(ans)
        
    return build(s) == build(t)

print(backspaceCompare("ab#c", "ad#c"))



