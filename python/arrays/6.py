def self_dividing_numbers(left, right):
    res = []

    def self_dividing(num):
        for c in str(num):
            if int(c) == 0 or num % int(c) > 0:
                return False
        return True

    for c in range(left, right + 1):
        if self_dividing(c):
            res.append(c)
    
    return res

print(self_dividing_numbers(47, 85))