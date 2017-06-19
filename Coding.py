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
