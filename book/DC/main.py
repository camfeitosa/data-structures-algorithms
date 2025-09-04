def soma(lista):
  total = 0
  for x in lista:
    total += x
  return total

print("Soma com Iteração", soma([1,3,6]))


# Dividir para Consquistar 

# Soma 
# Caso base -> pense no caso mais simples pra soma 
  # 🟢 Se tiver um Array com 0 ou 1? A soma vai ser 0 ou o próprio número
  # Caso base encontrado

def rec_soma(lista):
  if lista == []: # caso base
    return 0
  print("Rec", lista)
  return lista[0] + rec_soma(lista[1:])

print(rec_soma([1, 2, 3]))

# 🔴 Caso Base Array == [] 👇🏼 Volta para completar Chamada da função
# 3️⃣º lista = [3] || 3 + rec_soma([]) || 3 + [] = 3
# 2️⃣º lista = [2, 3] || 2 + rec_soma([3]) || 2 + 3 = 5 
# 1️⃣º lista = [1, 2, 3] (caso recursivo) 🟢 1 + rec_soma([2, 3]) -> slice [1:] começa no i 1 vai até o final || 1 + 5 = 6 🏆

# Função recursiva que conta números em uma lista
# Caso base -> uma lista vazia teria 0 itens -> caso mais simples
def contar(lista): 
  if lista == []:
    return 0

# Encontrar o valor mais alto em uma lista




# Caso base e resursivo para a pesquisa binária
