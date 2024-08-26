from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left:int = 0
        total:int = 0
        minLen:int = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min:int = right-left+1
                if minLen == 0 or min < minLen:
                    minLen = min    
                total-=nums[left]
                left+=1
        return minLen     