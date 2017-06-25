1.判断一个字符串是不是回文字符串
  #方法1:利用list的reverse()方法，不过需要注意的是list是一个可变对象#
def main():
	s="abcbad"
	l=list(s)
	k=l[:]
	k.reverse()
	if l==k:
		print "shi huiwen"
	else:
		print "bushi"
if __name__ == '__main__':
	main()
    #方法2:利用前后是否相等#
def main():
	s="aaaadfdfdf"
	count=0
	for i in range(0,len(s)/2):
		if s[i:i+1]==s[len(s)-1-i:len(s)-i]:
			count+=1
	if count==len(s)/2:
		print "shi huiwen"
	else:
		print "bushi huiwen"
if __name__ == '__main__':
	main()

2.如果从一端什么都有的字符串中取出字母
#两种方法可以实现1.判断字符串中的字母是否属于24个字母 2.用正则表达式
def main():
	s="nihao,woshi ni da y!"
	zimu="abcdefghijklmnopqrstuvwxyz"
	k=""
	for i in s:
		if i in zimu:
			k=k+"".join(i)
	print k
if __name__ == '__main__':
	main()
	
3.翻转整数，有个坑点就是负数的情况
#知识点：切片[1:5]则输出就是从标号1到标号5 而range(0,5)只是输出0--4
def main():
	k=""
	s=-123
	if s>0:
		l=list(str(s))
		l.reverse()
		for i in l:
			k=k+"".join(i)
		print k
	else:
		l=list(str(s))
		l.reverse()
		for i in l:
			k=k+"".join(i)
		print "-"+k[:len(l)-1]


if __name__ == '__main__':
	main()

4.最大公约数与最小公倍数：解法：用辗转相除法先求出最大公约数，再通过公式：两个数相乘等于这两个数的最大公约数和最小公倍数的积。求出最小公倍数
    public static int commonDivisor(int n,int m){
    #辗转相除是用大的除以小的。如果n<m，第一次相当n与m值交换
    while(n%m!=0){
    int temp=n%m;
    n=m;
    m=temp;
    }
    return m;
    }
    #求最小公倍数
    public static int commonMultiple(int n,int m){
    return n*m/commonDivisor(n,m);
}

5.求质数以及判断一个数是否是素数
  eg1.判断1到100之间的素数有哪些
       public static void main(String[] args) {
        int sum=0;
        int j;
        for (int i = 2; i <= 100; i++) // 1不是素数，所以直接从2开始循环
        {
            j = 2;
            while (i % j != 0) {
                j++; // 测试2至i的数字是否能被i整除，如不能就自加
            }
            if (j == i) // 当有被整除的数字时，判断它是不是自身
            {
                System.out.println(i); // 如果是就打印出数字
            }
        }
    }
}
  eg2.判断一个数是否是素数（质数就是只能被1和它本身整除的数）
    int a=cin.nextInt();
		System.out.println(a);
		for(int i=2;i<=a;i++){
				if(a%i==0){
					if(a!=i){
						System.out.println("this is not sushu");
					}else{
						System.out.println("this is sushu ");
					}
					break;
				
			}
}

6.判断字符串是否没有重复字符.实现一个算法确定字符串中的字符是否均唯一出现
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
7.递归实现阶乘
def refunc(n):
	i=1
	if n>1:
	  i=n
	  n=n*refunc(n-1)
        print "% d!="%i,n
        return n
8.斐波那契数列实现
方法一：
def fib(n):  
    a,b = 0,1  
    for i in range(n):  
        a,b =b,a+b  
    print a  
f = fib(10)  
print f 
方法二：
def fib(n):  
    """ 
    This is Fibonacci by Recursion. 
    """  
    if n==0:  
        return 0  
    elif n==1:  
        return 1  
    else:  
        return fib(n-1) + fib(n-2)  
  
if __name__ == "__main__":  
    f = fib(10)  
    print f  

9.桶排序：工作的原理是将数组分到有限数量的桶子里。每个桶子再个别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）
方法一：时间复杂度o(n)
def bucket(alist):
	n = len(alist)
	result=[0]*10
	print result
	for i in range(n):
		if alist[i] not in result:
			result[alist[i]-1]+=1
	return result

resu= bucket([6,2,7,3,2,8])
for i in range(len(resu)):
	for j in range(resu[i]):
		print i,
方法二：只适用于连续的无重复的序列
def bucket_sort(aList):  
	n = len(aList)  
	result = [0 for i in range(n)]  
	for i in range(n):  
	    result[aList[i] - 1] = aList[i]  
	return result  

10.快速排序：快速排序的基本逻辑是这样的：每次随机挑选一个数组的元素，作为“枢轴”，然后扫描数组中其他的所有元素，将小于枢轴的，排列在枢轴的左侧，
大于枢轴的，排列在枢轴的右侧。然后再分别对枢轴左右两侧的部分数组进行快速排序（这是一个递归的逻辑），这样，当递归运算“触底”后
（每次需要快排的部分数组中只有一个元素），逐层返回，就最终得到排好序的数组了。
    def quick_sort(aList):  
        first = 0  
        # 设定需要扫描的数组首尾位置  
        last = len(aList) - 1  
        # 改变参数的快速排序函数  
        aList = quick_sort_helper(aList, first, last)  
        return aList  
      
      
    def quick_sort_helper(aList, first, last):  
        # 这种情况说明扫描的数组部分只有一个元素了，直接返回  
        # 需要注意的是，原地排序没有真正意义上分割数组  
        # 只是对数组的不同部分做交换位置操作  
        # 所以“触底”后返回的是整个数组  
        if first >= last:  
            return aList  
        # 建立“枢轴”，不失一般性，令枢轴为扫描部分的第一个元素     
        pivot = aList[first]  
        # 计数，求出比枢轴小的元素的个数（也就是需要调整到的位置索引）  
        count = first  
        for index in range(first + 1, last + 1):#扫描  
            if aList[index] < pivot:  
                count += 1  
                # 交换位置  
                aList[index], aList[count] = aList[count], aList[index]  
        aList[count], aList[first] = aList[first], aList[count]  
        quick_sort_helper(aList, first, count - 1)  
        # 递归运算  
        quick_sort_helper(aList, count + 1, last)  
        return aList  

11.合并排序数组
def mergeSortedArray(self, A, B):  
        nA = len(A)  
        nB = len(B)  
        result = []  
        index_A = index_B = 0  
        # 两个指针都不能越界  
        while index_A != nA and index_B != nB:  
            if A[index_A] < B[index_B]:  
                result.append(A[index_A])  
                index_A += 1  
            else:  
                result.append(B[index_B])  
                index_B += 1  
        # 与未被扫描的部分合并，因为都是排好序的数组，所以直接相加  
        result += A[index_A:]  
        result += B[index_B:]  
        return result  
        # write your code here  
	
第二种情况：
	def mergeSortedArray(self, A, m, B, n):  
        # 实际上用m，n，total代表三个指针  
        total = m + n  
        while m > 0 and n > 0:  
            if A[m - 1] > B[n - 1]:  
                A[total - 1] = A[m - 1]  
                m -= 1  
            else:  
                A[total - 1] = B[n - 1]  
                n -= 1  
            total -= 1  
        # 如果是B没扫描完，依次对未赋值的A元素赋值  
        while n > 0:  
            A[total - 1] = B[n - 1]  
            n -= 1  
            total -= 1  
        return A  
        # write your code here  
12.查找字符串
题目描述：对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

样例：如果 source = "source" 和 target = "target"，返回 -1。如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。

    class Solution:  
        def strStr(self, source, target):  
            if source is None or target is None:  
                return -1  
            cur, index = 0, 0  
            s_len = len(source)  
            t_len = len(target)  
      
            # cur为当前target与source尝试匹配时，source的起始位置  
            while cur <= s_len - t_len:  
      
                # 记录一个临时值  
                temp = cur  
      
                # 扫描target  
                while index != t_len:  
                    # 匹配失败  
                    if target[index] != source[cur]:  
                        break  
                    # 当前字符匹配成功  
                    else:  
                        index += 1  
                        cur += 1  
      
                # index == t_len证明整个模式匹配成功  
                if index == t_len:  
                    return cur - t_len  
      
                # 若target没有匹配成功，向右移动一位，接着来  
                cur = temp + 1  
      
                # 负责扫描target的指针归零  
                index = 0  
            return -1  
13.字符串置换：利用字符串排序，有个重要知识点就是字符串转成列表然后转换成字符串
	def stringPermutation(A, B):
        if len(A)!=len(B):
            return False
        
        a=list(A)
        b=list(B)
        a.sort()
        b.sort()
        A="".join(a)
        B="".join(b)
        if A==B:
            return True
        else:
            return False
14.字符串空格替换，将空格替换为%20
def stringPermutation(s):
	k=s.split(" ")#通过split函数可以将字符串转换成数组
	m=""
	for i in range(len(k)-1):
		m=m+"".join(k[i])+"%20"

	m=m+"".join(k[len(k)-1])
	print m
15.删除元素，将列表中元素删除，这里有个知识点就是list中的remove方法不能再迭代的过程中使用，因为会造成长度不确定
def stringPermutation(a,elem):
	count=0
	for i in a:
		count+=1
	for j in range(count):
		a.remove(elem)
16.比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母
def compareStrings(A, B):
        # write your code here
        if len(A)==1 and len(B)==0:
            return True
        count=0

        f=[False]*len(A)
        

        for i in range(len(A)):
        	for j in range(len(B)):
        		if (A[i]==B[j]) and f[j]==False:
        			f[j]=True
        			count+=1
        			break
        if count==len(B):
        	return True
        else:
        	return False
