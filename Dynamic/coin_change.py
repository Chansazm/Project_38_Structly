import math
def counting_change(amount, coins):
    return _counting_change(amount, coins, 0)


def _counting_change(amount, coins, i):
    if amount == 0:
        return 1
    if i == len(coins):
        return 0
    coin = coins[i]
    total_ways = 0
    for qty in range((amount)+1):
        remainder = amount - (qty*coin)
        total_ways += _counting_change(remainder, coins, i + 1)
    
    return total_ways


print(counting_change(4, [1, 2, 3]))
print(math.factorial(40))
