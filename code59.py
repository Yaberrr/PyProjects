class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        #横轴及纵轴最大最小值
        arr:list = [0,0,n,n]
        #起始位置
        point:list = [0,0]
        result:list = [[0 for _ in range(n)] for _ in range(n)]
        m:int = 0
        while m < n:
            for i in range(4):
                isX:bool = i%2 == 0
                begin:int = point[0] if isX else point[1]
                end:int = (arr[i]+2)%4
                const:int = (arr[i]+1)%4
                step:int = 1
                if i >= 2:
                    step = -1
                    temp = begin
                    begin = end 
                    end = temp
                for j in range(begin,end,step):
                    m+=1
                    if isX:
                        result[const][j] = m
                        point[0] = end
                    else:
                        result[j][const] = m
                        point[1] = end         
                arr[i] += step
                
        return result
            
                
            
                
                            
                
                
                    
                    
                
            
            