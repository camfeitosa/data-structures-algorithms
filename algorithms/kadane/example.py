def max_subarray_sum(nums):
    max_soma_global = nums[0]
    
    max_soma_atual = 0
    
    for numero in nums:
        max_soma_atual += numero
        
        if max_soma_atual > max_soma_global:
            max_soma_global = max_soma_atual
            
        if max_soma_atual < 0:
            max_soma_atual = 0
            
    return max_soma_global

# Testando com o exemplo
nums_exemplo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"A maior soma do subarray é: {max_subarray_sum(nums_exemplo)}")



# Algoritmo de Kadane
def max_subarray_kadane(nums):
    max_atual = max_global = nums[0]

    for num in nums[1:]:
        max_atual = max(num, max_atual + num)
        if max_atual > max_global:
            max_global = max_atual

    return max_global

# Exemplo
lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_kadane(lista))  # Saída: 6