1.##########设计一个算法，计算出n阶乘中尾部零的个数##############
##########样例：11! = 39916800，因此应该返回 2###############
class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
      if n < 0:
          return -1
      count = 0
      for i in range(5,n+1):
          j=i
          while (j%5 == 0) : 
            count=count+1  
            j /= 5   
      return count
"""
因为尾零得来是由于2*5等于10，那么就会为结果增加一个零，所以只要计算这两个数出现了多少对就可以了。但是由于2出现的次数会远远大于5，
所以，只要计算5的倍数出现多少次。
"""

2.#############计算数字k在0到n中的出现的次数，k可能是0~9的一个值############
##########样例 n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)
class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        count = 0
        for i in range(0,n+1):
            l = list(str(i))
            count+=l.count(str(k))
        return count
"""
python中list.count()是统计列表中某个对象的个数，这道题的坑就在于它不是数字有多少个重复的，而是看字符有多少重复的。
str(i)将一个数字转换成字符格式。如11转换成字符形式为['1','1']
"""

3.############在数组中找到第k大的元素(不考虑重复的情况)#################
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        s = sorted(A)
        if k==1:
            return s[len(s)-1]
        else:
            return s[len(s)-k]
"""
python中可以直接排序sorted().还有一个输出列表下标的函数list.index()
"""
4.###########给定一个排序的整数数组（升序）和一个要查找的整数target，
用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。##########
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        low = 0
        height = len(nums)-1
        while low <= height:
            mid = (low+height)/2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                height = mid - 1
            else:
                return nums.index(target)
        return -1
"""
这就是考察二分法但是有个坑就是返回目标数字的下标，所以需要用list.index(target)
"""

5.################合并两个排序的整数数组A和B变成一个新的数组。###################
#####################样例给出 A = [1, 2, 3, empty, empty], B = [4, 5]合并之后 A 将变成 [1,2,3,4,5]#############
class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        for i in range(n):
            A[m+i]=B[i]
        A.sort()
        return A
"""
题目不难，重要的是利用python的特性的这种想法很关键
"""
6.##############给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。
你可以假设在数组中无重复元素。#############################
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A==None:
            return 0
        if len(A)==0:
            return 0
        start = 0
        end = len(A)-1 
        while start<=end:
            median = (start + end)/2
            if A[median] == target:
                return median
            elif A[median] < target:
                start = median + 1
            else:
                end = median - 1
        return start
"""
这道题虽然看似简单但是有一个比较需要注意的地方。就是给的数字是位于列表不存在，但是需要插入列表两侧的位置。如[1,2,4,5]，0或9
当0时，列表中没有我需要插入0的位置，但是如果用return end，则最后会返回-1，所以只能用return start .而插入9时，start是加的，只会打出
下标位置，但不会出错
"""
7.##############对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。
如果不存在，则返回 -1##########################################
class Solution:
    def strStr(self, source, target):
        # write your code here
        if source==None or target ==None:
            return -1
        if len(target)==0:
            return 0 
        sourcelen = len(source)
        targetlen = len(target)
        for i in range(sourcelen):
            k = i
            for j in range(targetlen):
                if(k<=sourcelen-1):
                    if source[k]==target[j]:
                        if j==targetlen-1:
                           return i
                        k+=1
                    else:
                      break
                else:
                  break
        return -1
"""
这到题的坑主要是如bdefe,efea这种情况会第一个字符串最后比对完，然而第二个还没比对完的情况
知识点：将一个字符串转换成字符数组遍历。列子s='sfdfsdf' k=range（len(s)）最后的输出结果是[0,1,2,3,4,5,6]
"""
"""
