class Solution:
    def reverseWords(self, s: str) -> str:
        reverse:str = ""
        lastIndex:int = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] != " " and lastIndex == -1:
                lastIndex = i 
            elif s[i] == " " and lastIndex != -1:
                reverse += s[i+1:lastIndex+1] + " "
                lastIndex = -1
                
        if lastIndex != -1:
            reverse += s[0:lastIndex+1]     
        elif reverse[-1] == " ":
            reverse = reverse[:-1]      
        return reverse                             
                
                
    
    