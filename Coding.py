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
  
