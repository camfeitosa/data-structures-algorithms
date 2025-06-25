def containsDuplicate(nums):
  dic = {}

  for i in range(len(nums)):
      cur = nums[i]

      if (cur in dic):
          return True

      dic[cur] = i
  return False

print(containsDuplicate([10, 10, 23, 12]))