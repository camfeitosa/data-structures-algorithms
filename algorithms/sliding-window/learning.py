# Soma máxima de subarray fixo

# Dado um array de inteiros e um número k, encontre a maior soma de qualquer subarray de tamanho k.
# (Exemplo: [2, 1, 5, 1, 3, 2], k=3 → 9, pois [5,1,3])

#  Slinding Window
def max_sum(arr, k):
  left = 0
  right = 0 # o right já é o número do iterador i
  max_sum = 0
  contador = 0
  dic = {}
  
  for i in range(len(arr)):
    if contador > k - 1:
      left = i
      right = i
      
    max_sum += arr[i]
    right+=1
    print(max_sum)
    
# print(max_sum([1, 3, 5, 7, 1, 4], 3))
# Tudo errado ☝🏼


# 🟢 Mesma questão 👇🏼
# Substring sem repetir caracteres
# Não passava no seguinte teste  "dvdf"
def lengthOfLongestSubstring(s):
    dic = {}
    max_len = 0 
    l = 0 # não sabia como deslizar essa left para direita

    for i in range(len(s)):
        if s[i] in dic:
            dic = {}
            
        dic[s[i]] = i
        curr_len = len(dic)
        max_len = max(max_len, curr_len)
    return max_len
  

# Passa em todos os teste
def lengthOfLongestSubstring2(s):
    l = 0
    dic = {}
    max_len = 0 

    for i in range(len(s)):
      # a b c a -> a repetido entra no if
        if s[i] in dic:
            l = dic[s[i]] + 1 # pega o indice do ultimo lugar que o caractere apareceu dic["a"] = 0
            dic[s[i]] = i 
            #dic['a'] = 0 → move l = 0 + 1 = 1
            # dic['a'] = 3 → atualiza a posição atual de 'a'
            # Agora a janela desliza para "bca", começando no índice 1.

        # a b c a -> a repetiu, entra no if 
        dic[s[i]] = i # adiciona a = 0, adiciona b = 1, adiciona c = 2
        max_len = max(max_len, i - l + 1) # 0 - 0 + 1 = 1 | 1 - 0 + 1 = 2 | 2 - 0 + 1 = 3 <-- até agora o l continua 0

    return max_len
  
  # Define o letft = 0 
  # Dicionario Vazio
  # Entra no for e verifica se o s[i] está no dicionário
    # Se tiver atualiza o valor de left para o indíce do valor repetido anterior + 1
    # Ex;
dic = {'a': 3, 'b': 5}
print(dic['a'] + 1) # retorna 4 
# atualiza dic com i atual

# Senão salva os valores no dic  dic[s[i]] = i -> "a": 0
# Faz o max de -> max(max_len, i - l + 1)  = 0 | 0 - 0 + 1 
  # Primeira iteração vai dar 1 


def lengthOfLongestSubstring3(s):
    l = 0
    dic = {}
    max_len = 0 

    for i in range(len(s)):
        if s[i] in dic and dic[s[i]] >= l: # é importante: só movemos l se o caractere repetido estiver dentro da janela atual. 
            l = dic[s[i]] + 1
            dic[s[i]] = i 
            
        dic[s[i]] = i
        max_len = max(max_len, i - l + 1)
    return max_len