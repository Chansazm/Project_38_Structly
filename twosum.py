def pair_sum(numbers, target_sum):
  map = {}
  for k,v in enumerate(numbers):
    difference = target_sum - v
    if k not in map:
      map[k] = difference
    map[difference] = v
      
  return (k,map[difference])
print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)

"""
0. Add indices and values to the storage if not already in the storage
    {3:0, 2:1,5:2,4:3,1:4}
1. calculate the difference of target_sum (8) - number in the list(3) = 5
2. look for the (5) difference in the map 
3. if difference (5) is in the data structure 
4. return the indices as a tuple of current location and diff location

def twosum(nums,target):
    values_map = {}
    for key,value in enumerate(nums):
        values_map[value] = key
        diff = target - value
        if diff in values_map:
            return [key, values_map[diff]]

#Driver function
nums = [2,5,7,4]
target = 9
print(twosum(nums,target))

"""