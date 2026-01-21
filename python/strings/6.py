def isPrefixString(s, words):
    c = "".join(words)
    n = len(s)

    return c[0:n] == s 

isPrefixString("iloveleetcode", ["i","love","leetcode","apples"])

