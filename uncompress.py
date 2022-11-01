def uncompress(s):
  str = []
  i = 0
  j = 0
  while j < len(s):
    if s[j].isdigit():
      j += 1
    else:
      num = s[i:j]
      string = num * int(s[j])
      str.append(string)
      j += 1
      i += 1
      
    
      
  return str

print(uncompress("2c3a1t")) # -> 'ccaaat'