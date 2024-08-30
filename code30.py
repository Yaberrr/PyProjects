from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        result:list[int] = []
        m:int = len(words)
        n:int = len(words[0])
        for i in range(n):
            map = Counter(words)
            count:int = len(map)
                
            #移动窗口     
            left,right = i,i
            while right+n <= len(s):
                rword = s[right:right+n]
                if rword in map:
                    if map[rword] == 0:
                        count+=1
                    elif map[rword] == 1:
                        count-=1    
                    map[rword] -= 1         
                right = right+n

                if right > left+n*m:
                    lword = s[left:left+n]
                    if lword in map:
                        if map[lword] == 0:
                            count+=1
                        elif map[lword] == -1:
                            count-=1  
                        map[lword] += 1 
                    left = left+n    
                
                if count == 0:
                    result.append(left)    
                        
                
        return result         
                