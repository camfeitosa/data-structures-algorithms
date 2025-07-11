def reverseWords(str):
        res = ''
        l, r = 0, 0 # l = ponteiro left, r = ponteiro right

        while r < len(str):
            if str[r] != ' ':
                r += 1
            else: 
                res += str[l:r+1][::-1] # inverter ::-1
                r += 1
                l = r
        res += ' '
        res += str[l:r + 2][::-1]
        return res[1:]
    
print(reverseWords('Camila'))