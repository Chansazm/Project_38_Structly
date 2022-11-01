def anagrams(s1, s2):
  result1 = ''.join(sorted(s1))
  result2 = ''.join(sorted(s2))
  i = 0
  j = 0
  
  while i < len(result1):
    if result1[i] != result2[j]: 
        return False
    i += 1
    j += 1
  return True

print(anagrams('restful', 'fluster')) # -> True