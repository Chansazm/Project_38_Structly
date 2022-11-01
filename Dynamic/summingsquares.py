import math


def summing_squares(n):
  return _summing_squares(n,{})


def _summing_squares(n,memo):
  if n in memo:
    return memo[n]
  if n == 0:
    return 0
  minimum = int(float('inf'))
  n = math.floor(math.sqrt(n)) + 1
  for i in range(1,n):
    square = i * i
    minimum_squares = 1 + _summing_squares(n-square, memo)
    minimum = min(minimum,minimum_squares)
  memo[n] = minimum
  return memo[n]
    
print(summing_squares(1)) #1