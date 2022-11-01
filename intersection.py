def intersection(a, b):
  seta = set(a)
  setb = set(b)
  return seta.intersection(setb)

print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]