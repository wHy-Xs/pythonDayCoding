'''
1.旋转数组中寻找最小值：旋转数组就是123456,456123这种格式的数组叫旋转数组。最直观简单的方法找最小值就是排序然后输出最小的那个，但是时间复杂度肯定高。所以
这里提出了一种新的思路。二分法查找的思路。

题目描述：假设一个旋转排序的数组其起始位置是未知的（比如：0 1 2 4 5 6 7 可能变成是：4 5 6 7 0 1 2）。你需要找到其中最小的元素。你可以假设数组中不存在重复的元素。
样例：给出[4,5,6,7,0,1,2]  返回 0
原理：首先，我们可以把一个排序数组先分割成两部分[first, second]，其中，first代表前面几个元素，second代表之后的，例如，对于数组[0, 1, 2, 4, 5, 6, 7]，可以设定first = [0, 1, 2], second = [4, 5, 6, 7]. 那么，经过旋转之后，
数组就变成了[second, first]，我们观察一下，这个新数组有这样两个特性：（1）second中所有元素都大于first中任意元素（2）second与first都是递增的序列

详细参考：http://blog.csdn.net/guoziqing506/article/details/51058549
'''
def findMin(self, num):  
        left, right = 0, len(num) - 1  
        while left < right and num[left] > num[right]:  
            mid = (left + right) // 2  
            # mid指在second中  
            if num[left] <= num[mid]:  
                left = mid + 1  
            # mid指在first中  
            elif num[left] > num[mid]:  
                right = mid  
        return num[left]  
