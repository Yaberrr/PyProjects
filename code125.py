class Solution:
    def isPalindrome(self, s: str) -> bool:
        first:int = 0
        last:int = len(s) - 1
        while first < last:
            while not s[first].isalnum() and first < last:
                first+1
            while not s[last].isalnum() and last > first:
                last-=1
            if s[first].lower() != s[last].lower():
                return False    
            else:
                first+=1
                last-=1
        return True        