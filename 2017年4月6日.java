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
