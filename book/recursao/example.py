# loop sem caso base
# def regressiva(i):
#   print(i)
#   regressiva(i - 1)

# regressiva(8)

# Caso recursivo - quando a função chama a si mesma
# Caso base - quando a função não chama a si mesma novamente

def regressiva(i):
  print(i)
  if i <= 1: # caso-base
    return
  else: # caso recursivo
    regressiva(i - 1)

regressiva(8)