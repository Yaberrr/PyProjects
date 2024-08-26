class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastword:int = 0
        flag:bool = False
        for letter in s:
            if letter != ' ':
                if flag:
                    lastword = 0
                    flag = False
                lastword +=1
            else:
                flag = True
        return lastword      