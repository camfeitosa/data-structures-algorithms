def buscaMenor(arr):
  menor = arr[0] # armazena o menor valor
  menor_indice = 0 # armazena o indice do menor valor
  
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice

print(buscaMenor([123, 345, 23, 9, 5]))


def ordenacaoSelecao(arr):
  novoArr = []
  
  for i in range(len(arr)):
    menor = buscaMenor(arr) # encontra o menor elemento ao array e adiciona no novo
    novoArr.append(arr.pop(menor)) # retira o elemento já adicionado no novo Array
    print("iteração", i)
  return novoArr

print(ordenacaoSelecao([12, 4, 5, 1829, 1, 10]))