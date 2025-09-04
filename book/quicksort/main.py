
def quicksort(array):
  len_arr = len(array)
  
  if len_arr < 2: # caso base
    return array
  else:
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([30, 15, 10, 1, 345, 56, 2, 67, 7, 79, 978, 9]))