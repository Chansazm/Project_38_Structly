def compress(s):
  s += '!'
  i = 0
  j = 0
  string = ""
  
  while j < len(s):
    if s[j] == s[i]:
      j += 1
    else:
      count = j-i
      if count == 1:
          string += s[i]
      else:
        string += str(count) + s[i]
      i = j
      
  return string


      
       

print(compress(('ccaaatsss'))) # -> '2c3at3s'