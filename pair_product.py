def pair_product(numbers, target_product):
  map = {}
  for indices, value in enumerate(numbers):
    map[indices] = value
    product = target_product//value
    if product in map:
      return (map[product],indices)

print(pair_product([2,4, 6, 8,9,9, 2], 16)) # -> (2, 3)