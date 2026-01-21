def maxProfit(days):
    min_price = days[0]
    max_profit = 0

    for price in days:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    
    return max_profit