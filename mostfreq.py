from collections import Counter
def most_frequent_char(s):
  map = Counter(s)
  most_frequent = 0
  for char in s:
    if map[char].values() > most_frequent:
      most_frequent = map[char].values()
      map[char].values()
  return most_frequent
    


print(most_frequent_char('bookeeper')) #e
