1.输入一个整数，将它翻转输出
  两种方法：1.利用字符串输入，然后s.charAt(i)进行逆向输出
           2.利用 StringBuilder a=new StringBuilder();
                 String m=a.append(12300).reverse().toString();
                 System.out.print(Integer.valueOf(m).intValue());这种方法有个缺陷就是末尾为0的话，会自动抹掉
           3.利用余数法
                  Scanner sc = new Scanner(System.in);  
                  System.out.println("请输入一个整数：");  
                  int num=sc.nextInt();  
                  int result=0;//存反转的数字  
                  while(true)  
                  {  
                      int n=num%10;//取出最低位上的数字  
                    //也可以直接打印出来System.out.println(n);但不好，也可以用一个数组存起来，也不好，都因为翻转后的前后的那个0的问题  
                      result=result*10+n;//依次的反转存储得到反转的数字  
                      num=num/10;//降位  
                      if(num==0)  
                      {  
                          break;  
                      }  
                  }  
                  System.out.println(result);  
