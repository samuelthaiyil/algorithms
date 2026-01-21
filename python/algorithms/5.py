def subtract_product_and_sum(n):
    sum_of_digits = 0
    product_of_digits = 1

    for c in str(n):
        sum_of_digits += int(c)
        product_of_digits *= int(c)

    return product_of_digits - sum_of_digits

print(subtract_product_and_sum(234))