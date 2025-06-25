def binary_search(nums, n):
  lo = 0
  hi = len(nums)
  steps = 0 
  
  # Quando o lower for igual ao higher, significa que não existe o número
  # Two pointers
  while lo < hi:
    steps+= 1
    mid = int((lo + hi)/2)
    
    if nums[mid] == n:
      print("steps", steps)
      return mid
    elif nums[mid] < n:
      lo = mid + 1
    else:
      hi = mid
  return -1

# Dobra o input
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Tempo continua linear
# O(log n) - logaritmico
binary_search(a, 3) # 1 step 
binary_search(b, 3) # 2 steps
binary_search(c, 3) # 3 steps
