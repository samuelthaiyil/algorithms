def buySellStock(prices):
    min_price = prices[0]
    max_profit = 0

    for d in prices:
        if d < min_price:
            min_price = d
        else:
            max_profit = max(max_profit, d - min_price)
    
    return max_profit
