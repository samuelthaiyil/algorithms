def replaceDigits(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz';

    def shift(letter, number):
        return alphabet[int(alphabet.index(letter)) + number]
    
    chars = list(s)

    for i in range(len(s)):
        if s[i].isalpha():
            chars[i + 1] = shift(s[i], int(chars[i + 1]))
    
    return "".join(chars)

print(replaceDigits("a1c1e9"))       


        
