1.给出一个非负整数 num，反复的将所有位上的数字相加，直到得到一个一位的整数。
  eg:给出 num = 38,相加的过程如下：3 + 8 = 11，1 + 1 = 2。因为 2 只剩下一个数字，所以返回 2。
      public static void main(String[] args) {	
        int a=1243;
        int sum=0;
        int numbit=0;
        System.out.println("dddd");
        while(true){
            while(a!=0){
              numbit=a%10;//这一步是取最后一位数
              sum+=numbit;//求和
              a/=10;//舍弃最后一位
          }	
          if(sum<10)
            break;
          a=sum;
          sum=0;
        }
      }
2.x的n次幂
  思路：考虑到一种特殊的情况就是当num==0时，它的不管多少次幂都是1.另一个坑点就是要考虑幂次负数的情况。
  public double myPow(double x, int n) {
        // Write your code here
        double sum=1;
        if(n>0){
            for(int i=0;i<n;i++){
              sum=sum*x;
               }
            }else if(n<0){
              for(int j=n;j<0;j++){
                sum=sum*(1/x);
              }
            }else if(n==0){
                 sum=1;
            }
            return sum;
         }
3.求质数以及判断一个数是否是素数
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
4.落单的数
''' 
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

		int[]arr={1,2,2,1,3,5,3};
		int n=arr[0];
		for(int i=1;i<arr.length;i++){
			n=n^arr[i];				
		}
		System.out.println(n);
'''
