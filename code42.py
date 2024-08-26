from typing import List

class Solution:
    def trap2(self, heightArr: List[int]) -> int:
        total:int = 0
        stack:List[int] = []
        for index,height in enumerate(heightArr):
            while stack and heightArr[stack[-1]] < height :
                top = stack.pop()
                if stack:
                    before = stack[-1]
                    total += (index-before-1)*(min(heightArr[before],height)-heightArr[top])
            stack.append(index)    
        return total
    
    def trap3(self, heightArr: List[int]) -> int:
        total:int = 0
        left:int = 0
        right:int = len(heightArr)-1
        leftMax:int = 0
        rightMax:int = 0
        while left < right:
            leftMax = max(leftMax,heightArr[left])
            rightMax = max(rightMax,heightArr[right])
            if heightArr[left] < heightArr[right]:
                total += (leftMax - heightArr[left])
                left += 1   
            else:     
                total += (rightMax - heightArr[right])
                right -= 1
        return total           
                
            
                            
    
    def trap1(self, heightArr: List[int]) -> int:
        volume:int = 0
        length:int = len(heightArr) 
        if length < 3:
            return 0
        leftMaxArr:List[int] = (0)*length
        rightMaxArr:List[int] = (0)*length
        for i in range(1,length):
            leftMaxArr[i] = max(leftMaxArr[i-1],heightArr[i-1])
        for i in range(length-2,0,-1):
            rightMaxArr[i] = max(rightMaxArr[i+1, heightArr[i+1]])
        
        for i in range(length):
            height:int = min(leftMaxArr[i],rightMaxArr[i])
            if heightArr[i] < height:
                volume += height - heightArr[i]
        return volume         
                
            
                            