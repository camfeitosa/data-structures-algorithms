def is_palindrome(string):
  
  newStr = ''.join(filter(str.isalnum, string)).lower()
  l = 0 
  r = len(newStr) - 1
  
  while l < r:
    if newStr[l] != newStr[r]:
      return False
    else:
      l += 1
      r -= 1
  return True

print(is_palindrome("Arara e ana    "))

def simple(text):
  processed_text = ''.join(filter(str.isalnum, text)).lower()
  return processed_text == processed_text[::-1]

print(simple("Arara"))

print(5 == -5 )