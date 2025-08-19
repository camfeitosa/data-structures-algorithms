# call stack

def sauda(nome):
  print("Olá, " + nome)
  sauda2(nome)
  
  print("preparando para dizer tchau...")
  tchau()
  
def sauda2(nome): 
  print("Como vai, " + nome + " ?")
  
def tchau():
  print("ok, tchau")
  
  
sauda("Camila")

# recursão
def fatorial(x):
  if x == 1: # caso-base
    return 1
  else:
    return x * fatorial(x - 1) # (caso recursivo)
  
print(fatorial(3)) 
 

# 👇🏼👇🏼 acaba aqui 👇🏼👇🏼

# 1️⃣º x = 3 || 3 * 2 || 🔴 Retorna 6 
# 2️⃣º x = 2 (o x armazenado na função não muda) || 2 * retorno de fatorial(x-1) || 2 * 1 || 🔴 Retorna 2

# Chamadas anteriores não foram finalizadas - necessário tirar os itens da pilha

# 3️⃣º x = 1 (caso base) 🔴 Return 1 - primeiro retorno
# 2️⃣º x = 2 (caso recursivo) 🟢 2 * fatorial(2 - 1)
# 1️⃣º x = 3 (caso recursivo) 🟢 3 * fatorial(3 - 1)

# ☝🏼☝🏼 começa daqui☝🏼☝🏼

# call stack 
# pilha -> adiciona um item
#       -> retira o item de cima
#       -> LIFO