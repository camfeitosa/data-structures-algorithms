def max_sum(arr, k):
    # 1) soma inicial da primeira janela [0..k-1]
    window_sum = sum(arr[:k])
    max_sum = window_sum
    left = 0

    # 2) desliza a janela: right vai de k até o fim
    for right in range(k, len(arr)):
        # entra arr[right], sai arr[left]
        window_sum += arr[right] - arr[left]
        left += 1  # andou a borda esquerda
        max_sum = max(max_sum, window_sum)

    return max_sum


# Subarray média máxima - LeetCode
# somar os k elementos e dividir por k

def findMaxAverage(nums, k):
    window_sum = sum(nums[:k]) 
    max_sum = window_sum
    left = 0

    if len(nums) == 1:
        return window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[left] # soma anterior + valor atual i - left antigo
        left+=1
        max_sum = max(max_sum, window_sum)
    return max_sum / k
  
print(findMaxAverage([12, 34, 5,6 ,6 ,72,3], 5))

# Explicação 
# nums[a:b] => slice

arr = [1, 4, 6, 8, 9]
k = 3

print(arr[:k]) # slice do índice 0 até o índice 2 (3 primeiros elementos)
# retorna [1, 4, 6]

#sum() -> soma os valores de um iteravel (array)
soma = sum([2, 5, 1])
print(soma) # retorna 8

print(sum(arr[:k])) # soma dos k primeiros elementos

# max() -> retorna o valor máximo entre os valores dentro de max
print("Valor maximo", max(2, 5, 9)) # retorna 9
# max_sum = max(max_sum, calculo_atual) -> retorna qual o valor máximo entre o valor guardado antigo e o atual


# janela deslizante vai atualizar o valor de left para left += 1 e iterar o valor de right para i+=1

k = 3
[1, 2, 3, 4, 5, 6]
[1, 2, 3] # primeira janela = 6

# iteração começa no índice 3 
[2, 3, 4] # segunda janela = 9

# left += 1
[3, 4, 5] # 9 (soma anterior) + 5 (iteração atual do i) - 2 (left antigo)  = 12
# soma anterior + valor atual i - left antigo
# janela desliza para a direita, ou seja, um valor da esquerda sai e um valor da direita entra

# 1 - Definir a soma atual da janela
# 2 - Definir valor de left
# 3 - Definir a var max_sum
# 4 - Na iteração fazer o cálculo atual
# 5 - Comparar qual é maior - max_sum ou calculo_atual