def sum(num): 
    arr = {}

    for i in range(1, num):
        arr[i] = num

    for i in arr:
        cur = arr[i]
        x = cur - num
        
        if (x in arr):
            return arr.get(x), i
    return -1

print(sum(11))






