from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        letter_dict:dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total:int = letter_dict[s[-1]]
        i:int = 0
        for i in range(len(s)-1):
            if letter_dict[s[i]] < letter_dict[s[i+1]]:
                total -= letter_dict[s[i]]
            else:
                total += letter_dict[s[i]]  
        return total    
                

solution = Solution()
result = solution.romanToInt("MCMXCIV")
print(result)  # 输出: 1994