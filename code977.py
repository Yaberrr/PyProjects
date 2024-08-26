from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left:int = 0
        right:int = len(nums)-1
        new_nums:List[int] = [None]*len(nums)
        i:int = right
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                new_nums[i] = nums[right]**2
                right-=1
            else:
                new_nums[i] = nums[left]**2
                left +=1
            i-=1
        return new_nums
                