def position(costs, pos=0):
    prices = []
    for index, value in enumerate(costs[pos]):
        price = costs[pos]
        prices.append(price)
        pos = pos + 1
    return prices
    



costs = [
  [4, 3, 7],
  [6, 1, 9],
  [2, 5, 3]
]
print(position(costs, 0))