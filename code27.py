from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow:int = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow+=1
        return slow     