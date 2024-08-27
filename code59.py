class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result:list = [[0 for _ in range(n)] for _ in range(n)]
        right,bottom,left,top = n,n,0,0
        x,y = 0,0
        value = 0
        while value <= n:
            for x in range(x, right+1):
                result[y][x] = value
                value += 1
            top+=1
            
            for y in range(y, bottom+1):
                result[y][x] = value 
                value+=1
            right-=1
            
            for x in range(x,left-1,-1):
                result[y][x] = value 
                value+=1
            bottom-=1
            
            for y in range(y,top-1,-1):
                result[y][x] = value 
                value+=1 
            left+=1                    
                
        return result  
                    
                
            