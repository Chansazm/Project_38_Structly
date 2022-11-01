def token_replace(s, tokens):
  i = 0
  j = 1
  output = []
  while i < len(s):
    if s[i] != '$':
      output.append(s[i])
    elif s[i] == '$':
      j += 1
    else:
      key = s[i:j]
      i+= 1
      
  print(output)
        
   
tokens = {
  '$greeting$': 'hey programmer',
}
print(token_replace('his greeting is always $greeting$...', tokens)) 
# -> 'his greeting is always hey programmer.'
#strategy
#two pointers
#conditions
#