'''
给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序
注意事项
1.必须在原数组上操作
2.最小化操作数
样例:给出 nums = [0, 1, 0, 3, 12], 调用函数之后, nums = [1, 3, 12, 0, 0].
'''
'''
这道题如果不需要原地操作，则很简单
'''
1.1.不是原数组操作
def moveZeroes(self, nums):
        r=[]
        res=[]
        k=0
        m=0
        for i in range(len(nums)):
            if nums[i]==0:  #如果遍历等于0则存入r数组
                r.append(nums[i])
                k+=1
            else:     #如果遍历不等于0，则存入res数组
                res.append(nums[i]) 
                m+=1
        res.extend(r) #将两个数组整合
        return res
'''思路:先设置两个空数组用于装非0的数据和为0的数据，最后整合的一起'''
1.2.第二种思路原数组操作：
def moveZeroes(self, nums):
        #这种方法不是原数组操作
        if nums is None:  
            return nums  
        left, n = 0, len(nums)  
  
        # 下面的循环使得left指向数组的第一个0  
        while left < n:  
            if nums[left] == 0:  
                break  
            left += 1  
        right = left + 1  
  
        # 下面的循环使得right指向left之后数组的第一个非0数  
        while right < n:  
            if nums[right] != 0:  
                break  
            right += 1  
  
        while right < n:  
  
            # 如果nums[right]非0，则与nums[left]交换  
            if nums[right] != 0:  
                nums[left], nums[right] = nums[right], nums[left]  
                # 令left与right各向前移动一位，这样做保证了left始终指向数组的第一个0  
                right += 1  
                left += 1  
  
            # 如果nums[right]为0，则令right向前移动，找非0的元素  
            else:  
                right += 1  
        return nums  
 '''思路：先找到第一个0的元素，然后找到第一个非0的元素，然后再交换两个的位置，重复上述操作'''
