class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m:int = len(t)
        arr = [[0]*26 for _ in range(m)]
        arr.append([m]*26)
        
        for i in range(m-1,-1,-1):
            for j in range(26):
                arr[i][j] = i if j + ord('a') == ord(t[i]) else arr[i+1][j]
            
        index = 0       
        for c in s:
            pos:int = arr[index][ord(c)-ord('a')]
            if pos == m:
                return False
            index = pos+1
        
        return True    