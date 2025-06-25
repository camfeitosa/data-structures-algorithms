def isPalindrome(s):

  newStr = ''.join(filter(str.isalnum, s)).lower()

  l, r = 0, len(newStr) - 1

  while l < r:
      if newStr[l] != newStr[r]:
          return False
      else:
          l += 1
          r -= 1
  return True
      
print(isPalindrome("Ana"))