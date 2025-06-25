def binary_search(arr, alvo):
  l, r = 0, len(arr) - 1
  
  while l < r:
    mid = l + r // 2
    
    if arr[mid] == alvo:
      return mid
    elif arr[mid] < alvo:
      l = mid + 1
    else:
      r = mid -1
      
  return -1

print(binary_search([10, 23, 345, 546, 2243, 4363], 1))
  