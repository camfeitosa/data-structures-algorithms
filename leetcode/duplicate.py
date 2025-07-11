# usando dicionário // hashmap
# pega o valor atual da iteração nums[i]
  # verifica se o valor atual está no dicionário - chave
    # se tiver retorna True, senão adiciona o valor no dicionário dic[cur] <- chave = i <- indice do array atual 
    

def containsDuplicate(nums):
  dic = {}

  for i in range(len(nums)):
      cur = nums[i]

      if (cur in dic):
          return True

      dic[cur] = i
  return False

print(containsDuplicate([10, 10, 23, 12]))