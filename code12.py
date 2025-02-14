from typing import List
class Solution:
    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    
    def intToRoman(self, num: int) -> str:
        roman:str = ""
        for value in Solution.VALUE_SYMBOLS:
            while num >= value[0]:
                num -= value[0]
                roman += value[1]
            if num == 0:
                break    
        return roman        