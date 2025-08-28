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
# Utiliza para encontrar o subarray de soma máxima, mesmo com números negativos
def max_subarray_kadane(nums):
    max_atual = nums[0]
    max_global = nums[0]

    for num in nums[1:]:
        max_atual = max(num, max_atual + num) # numéro atual pode ser -4
        # e o número máximo anterior pode ser -2
        # entre -4 e (-2 - 4) = -6 ele analísa qual é o valor maior
        # seria o -4
        if max_atual > max_global: # se o máx_atual for maior que o máx_global
            # redefino o max_global
            max_global = max_atual

    return max_global

# Exemplo
lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_kadane(lista))  # Saída: 6