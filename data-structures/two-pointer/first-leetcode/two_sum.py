# Essa solução só serve para array ordenado

def twoSum(nums, target):
  l, r = 0, len(nums) - 1

  while l < r:
      soma = nums[l] + nums[r]
      if (soma == target):
          return (l, r)
      elif (nums[r] > target):
          r -= 1
      else:
          l += 1
  return -1
  
  
# Correto
def twoSumOk(nums, target):

    mapa = {}

    for i in range(len(nums)):
        atual = nums[i] 
        x = target - atual

        if (x in mapa):
            return mapa.get(x), i

        mapa[atual] = i
    return -1
  
#  exemplo target = 6, atual = 2
# 6 - 2 => o valor que preciso encontrar é 4 
# Se 4 estiver no mapa, retorna mapa.get(x) -> pega o index e i -> indice atual que somou + 4
 
array = [10, 30, 7, 0, 2, 4]
array = [1, 2, 3, 4, 5]
alvo = 6
print(twoSum(array, alvo))  


