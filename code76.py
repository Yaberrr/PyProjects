from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_str:str = ""
        #边界
        left:int = 0
        right:int = 0
        #记录每个字母出现的次数
        char_dict:dict[str,list[int]] = {}
        for c in t:
            if c in char_dict:
                char_dict[c][1] += 1
            else:
                char_dict[c] = [0, 1]  

        #窗口内已满足次数的字母总数
        current:int = 0   
        for right in range(len(s)):
            if s[right] in char_dict:
                arr = char_dict.get(s[right])
                arr[0] += 1
                #满足次数，字母总数加一
                if arr[0] == arr[1]:
                    current+=1 

                #当前窗口满足条件 判断该子串长度      
                while current == len(char_dict):
                    if min_str == "" or right+1-left < len(min_str):
                        min_str = s[left:right+1] 
                    #移动左边界
                    if s[left] in char_dict:
                        arr = char_dict.get(s[left])
                        arr[0] -= 1
                        #不满足次数，字母总数减一
                        if arr[0] == arr[1]-1:
                            current-=1  
                    left+=1    
        return min_str        
        