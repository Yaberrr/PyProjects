from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstStr = strs[0]
        for i in range(len(firstStr)):
            for str in strs[1:]:
                if len(str)-1 < i or str[i] != firstStr[i] :
                    return firstStr[:i]
        return firstStr        
            
            