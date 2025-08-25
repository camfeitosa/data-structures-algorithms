# Utilizando Set 
def maximumUniqueSubarray(nums):
    l = 0
    max_sum = 0
    curr_sum = 0
    seen = set()

    for i in range(len(nums)):
        while nums[i] in seen:
            seen.remove(nums[l])
            curr_sum -= nums[l]
            l += 1

        curr_sum += nums[i]
        seen.add(nums[i])
        max_sum = max(max_sum, curr_sum)
        

    return max_sum
  

# First
def maximumUniqueSubarray(nums):
    l = 0
    dic = {}
    max_sum = 0

    for i in range(len(nums)):
        if nums[i] in dic and dic[nums[i]] >= l:
            left = dic[nums[i]] + 1
            dic[nums[i]] = i
        
        dic[nums[i]] = i
        max_sum = max(max_sum, i - l + 1)
        

    return sum(dic)