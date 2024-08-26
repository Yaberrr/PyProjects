from typing import List

class Solution:
    def lengthOfNums(self,nums:List[int]):
        dp:List[int] = [1] * len(nums)
        maxLen:int = 1
        for i in range(1,len(dp)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1,dp[i])
            maxLen = max(maxLen,dp[i])
        return maxLen
    

solution = Solution()
nums = [0,1,0,3,2,3,5]
result = solution.lengthOfNums(nums)
print(result)