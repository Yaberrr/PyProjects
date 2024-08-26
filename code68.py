from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result:List[str] = []
        index:int = 0
        while index < len(words):
            #每行
            row:List[str] = []
            #行宽
            minWidth:int = 0
            #获取该行最多能塞几个单词
            while True:
                #获取新的一个单词
                word = words[index]
                #当前行宽+最小空格数(有几个单词则有几个空格)+新单词数(最后一个单词不需要空格)
                if minWidth + len(row) + len(word) <= maxWidth:
                    row.append(word)
                    minWidth += len(word)
                    index+=1
                else:
                    break
                #已到达所有单词中的最后一个单词,则必为最后一行
                if index >= len(words):
                    #最后一行 左对齐
                    new_word = " ".join(row)
                    result.append(new_word + (maxWidth-len(new_word))*" ")
                    return result
                
            #该行单词已确定 填充空格
            diff:int = maxWidth - minWidth
            if len(row) > 1:
                #平均每个单词用空格
                avg_space:int = diff//(len(row)-1)
                #多出来的空格 优先从左往右分配
                for i in range(diff%(len(row)-1)):
                    row[i] += " "
                result.append((" "*avg_space).join(row))   
            else:
                result.append(row[0] + (" "*diff))
        return result               
                
                
                