class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
       
        lista = [x, y, z]
        
        for i in range(z):
            
            if lista[0] < z:
                passos1 = z - lista[0]
            else:
                passos1 = lista[0] - z
                
            if lista[1] < z:
                passos2 = z - lista[1]
            else: 
                passos2 = lista[1] - z
    
            if passos1 < passos2:
                return 1 
            elif passos2 < passos1:
                return 2
            else:
                return 0
    
solution = Solution()

print(solution.findClosest(10, 20, 40))