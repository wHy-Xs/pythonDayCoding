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
