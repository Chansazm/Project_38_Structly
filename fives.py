def five_sort(nums):
  i = 0
  j = len(nums)
  
  while i < j:
    if nums[i] == 5 and nums[j] != 5:
      nums[i],nums[j] = nums[j],nums[i] 
    i += 1
    j -= 1
    
  return nums

"""
1. using two indices one at start and other at end
--> i = 0.  j = 7
2. on left find a five
--> 5
3. compare the num to the right side
 ---> 5 == 7
4. exchange 5 & 7
4. increament on left and decreament on right
6. return the list
"""
print(five_sort([12, 5, 1, 5, 12, 7]))
# -> [12, 7, 1, 12, 5, 5] 