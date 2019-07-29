def toChars(s): 
  s = s.lower() 
  letters = '' 
  
  for c in s:
    if c in 'abcdefghijklmnopqrstuvwxyz': 
      letters = letters + c
  return letters
