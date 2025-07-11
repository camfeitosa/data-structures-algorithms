def bubble(nums):
  size = len(nums)
  for _ in nums:
    is_sorted = True # otimizar para não percorrer o array inteiro
    print(nums)
    for i in range(size - 1):
      if nums[i] > nums[i+1]:
        is_sorted = False
        nums[i+1], nums[i] = nums[i], nums[i+1] # muda as posições
      if is_sorted:
        return

bubble([5,4,3,2,1])
print("Ordenado: ")
bubble([1,2,3,4,5])