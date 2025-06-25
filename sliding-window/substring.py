def maximumLengthSubstring(string: str) -> int:
  l, r = 0, 0
  _max = 1 
  counter = {}
  
  counter[string[0]] = 1
  
  # avança janela -> ponteiro r
  while r < len(string) - 1:
    r+=1
    if counter.get(string[r]):  
      counter[string[r]]+= 1 
    else:
      counter[string[r]] = 1
    
    # contrai janela -> ponteiro l
    while counter[string[r]] == 3:
      counter[string[l]] -=1
      l+=1
    _max = max(_max, r-l+1)
  return _max
  
    