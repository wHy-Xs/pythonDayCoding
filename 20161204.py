''' 
1.落单的数 
描述：给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。
'''
 def singleNumber(self, A):
        # write your code here
        if len(A)==0:
            return 0
        n = A[0]
        for i in range(1,len(A)):
            n = n ^ A[i]
        return n 
'''
知识：1.考虑A为空的情况 2.异或知识：相同为0，不同为1.a异或b异或a=b,a异或b异或b=a
'''
