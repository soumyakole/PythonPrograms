def calculate_max_profit(share_price_list):
    max_profit = 0
    lowest_price_so_far = float("inf")
    for price in share_price_list:
        lowest_price_so_far = min(lowest_price_so_far, price)
        profit = price - lowest_price_so_far
        max_profit = max(max_profit, profit)
        print('price', price, 'lowest_price_so_far', lowest_price_so_far, 'profit', profit, 'max_profit', max_profit)
    return max_profit

print(calculate_max_profit([250, 270, 230, 240, 222, 260, 294, 210]))
print(calculate_max_profit([70, 60, 50, 40, 30, 20, 10, 0]))
