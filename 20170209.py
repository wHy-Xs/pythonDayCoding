1.判断字符串是否没有重复字符.实现一个算法确定字符串中的字符是否均唯一出现
    class Solution:
        # @param s: a string
        # @return: a boolean
        def isUnique(self, str):
            # write your code here
            d={}
            for i in str:
                if i not in d:
                    d[i]=1
                else:
                    return False
            return True
