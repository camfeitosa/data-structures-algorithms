def hashmap_leetcode(nums):
  
  l, r = 0, len(nums) - 1
  dic = {}

  for i in range(len(nums)):
      cur = nums[i]
      print(cur)
      
      print(dic)
      if (cur in dic):
        return True

      dic[i] = cur
      print("Passo: ", dic)
  return False

print(hashmap_leetcode([3, 3]))

#  Resolvido

def containsDuplicate(nums):

    dic = {}

    for i in range(len(nums)):
        cur = nums[i]

        if (cur in dic):
            return True
          
        dic[cur] = i # dic[cur] = "chave": {i} -> o in pega o valor da chave do hashmap
    return False
  
print(containsDuplicate([3, 3]))


# Mais rápida 

def containsDuplicate(nums):
    seen = set()
    
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)

    return False