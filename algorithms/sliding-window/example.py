# Sliding Window
# É utilizado para resolver problemas de subarray ou substring
# onde é necessário manter uma janela de elementos contígua e ajustar seu tamanho dinamicamente.

def sliding_window_example(arr, k):
    """
    Exemplo de uso da técnica de janela deslizante para encontrar a soma máxima de um subarray de tamanho k.
    
    :param arr: Lista de inteiros
    :param k: Tamanho do subarray
    :return: Soma máxima do subarray de tamanho k
    """
    max_sum = 0
    current_sum = 0
    
    # Calcular a soma dos primeiros k elementos
    for i in range(k):
        current_sum += arr[i]
    
    max_sum = current_sum
    
    # Deslizar a janela pelo array
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum