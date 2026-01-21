def harshad_number(num):
    sum_of_digits = 0

    for c in str(num):
        sum_of_digits += int(c)
    
    if num % sum_of_digits == 0:
        return sum_of_digits
    else:
        return -1

print(harshad_number(23))