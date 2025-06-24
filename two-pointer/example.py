# Resolver problemas de array e strings usando a técnica de dois ponteiros.

# two pointers é uma técnica de resolução de problemas que utiliza dois ponteiros para percorrer uma estrutura de dados, como um array ou string, de forma eficiente. Essa técnica é especialmente útil para problemas que envolvem pares, subarrays ou substrings.

def two_pointer_example(arr, target):
    """
    Exemplo de uso da técnica de dois ponteiros para encontrar dois números em um array que somam um valor alvo.
    
    :param arr: Lista de inteiros
    :param target: Valor alvo para a soma
    :return: Tupla com os dois números que somam o valor alvo ou None se não encontrados
    """
    
    left, right = 0, len(arr) - 1
    arr.sort()  # Ordena o array para aplicar a técnica de dois ponteiros
 # soma o valor de left + right, 
 # se for igual ao target, retorna os dois números
 # se for menor que o target, incrementa o ponteiro left
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None
  

def two_pointer_pair(arr):
  l, r = 0, len(arr) - 1
  passo = 0
  
  while l < r:  
    passo += 1  
    if(arr[l] == arr[r]):
      return (f"Pares: {arr[l]}, {arr[r]}, Passos: {passo}")
    elif (arr[l] < arr[r]):
      l += 1
    else:
      r -= 1
  return -1


array = [2, 3, 4, 5, 6, 3]
print(two_pointer_pair(array))