import random


class RandomizedSet:
    def __init__(self) -> None:
        self.nums = []
        self.indices = {}
        
    def insert(self,val:int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True
    
    def remove(self,val:int) -> bool:
        if val not in self.indices:
            return False
        index = self.indices.pop(val)
        temp = self.nums.pop()
        if index != len(self.nums):
            self.nums[index] = temp
            self.indices[temp] = index
        return True
    
    def getRandom(self) -> int:
        return self.nums[random.randint(0,len(self.nums)-1)] 
    
        
    
    
    
    
    
    
        