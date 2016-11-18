#######用二分法查找数组中最小的元素#####################
class Solution:  
    # @param nums: The integer array  
    # @param target: Target number to find  
    # @return the first position of target in nums, position start from 0   
    def binarySearch(self, nums, target):  
          
        left, right = 0, len(nums) - 1  
          
        while left <= right:  
            mid = (left + right) // 2  
            # 即便nums[mid] == target，也要继续查左边的部分  
            if nums[mid] >= target:  
                right = mid - 1  
            else:  
                left = mid + 1  
          
        if left <= len(nums) and nums[left] == target:  
            return left  
              
        return -1  
        # write your code here  
#################################################################
1.#############给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：###
##############如果这个数被3整除，打印fizz.########################
##############如果这个数被5整除，打印buzz.########################
##############如果这个数能同时被3和5整除，打印fizz buzz.############
 def fizzBuzz(self, n):
        results = []
        for i in range(1, n+1):
            if i % 15 == 0:
                results.append("fizz buzz")
            elif i % 5 == 0:
                results.append("buzz")
            elif i % 3 == 0:
                results.append("fizz")
            else:
                results.append(str(i))
        return results
###############################################################
3.####求素数####################################################
def isSushu(n):
    if n<=1:
        return False
    i = 2
    while i*i < n:
        if n%i==0:
            return False
        i+=1
     return True 
###############################################################
"""
质数又称素数。指在一个大于1的自然数中，除了1和此整数自身外，不能被其他自然数整除的数。素数在数论中有着很重要的地位。
比1大但不是素数的数称为合数。1和0既非素数也非合数。质数是与合数相对立的两个概念，二者构成了数论当中最基础的定义之一。
"""
4.###############实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。##
#####你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。############
class MinStack(object):
    
    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minstack = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if len(self.minstack) == 0 or number <= self.minstack[-1]:
            self.minstack.append(number)

    def pop(self):
        # pop and return the top item in stack
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    def min(self):
        # return the minimum number in stack
        return self.minstack[-1]
"""
总体思想就是设置两个数组，一个装最小值，一个正常模拟stack
"""
5.############正如标题所述，你需要使用两个栈来实现队列的一些操作。###########
####队列应支持push(element)，pop() 和 top()，其中pop是弹出队列中的第一个(最前面的)元素。
#####pop和top方法都应该返回第一个元素的值。###################################
6#####求两个数的最大公约数（辗转相除法）#######################################
def gcd(a, b):
  if a < b:
    a, b = b, a
  while b != 0:
    temp = a % b
    a = b
    b = temp
  return a

k=gcd(0,0)
print k
##################################
"""
两个整数的最大公约数等于其中较小的数和两数的差的最大公约数
"""
