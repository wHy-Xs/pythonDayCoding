1.两个字符串链接两种方法：
  1.String a="absd";
    String b="dfdf";
    String c=a+b;
  2.String a="dfd";
    String c=a.concat("dfdfdf");

2.替换字符串
  String中的replace(old,new);replaceAll(regx，用什么替换regx匹配到的字符）;replaceFirst(regx,tongli)

3.求一个无序数组中第K大或第k小的数（可以）重复
  public static void main(String[]args){
    Scanner cin=new Scanner(System.in);
    int k=cin.nextInt();
    //int[]arr=new int[10];
    int[]a={1,2,3,4,4,5,6,6,3,2,1,4,};
    //排序
    for(int i=0;i<arr.length;i++){
      for(int j=0;j<arr.length-i-1;j++){
        if(arr[j]>arr[j+1]){
          int tmp=arr[j];
          arr[j]=arr[j+1];
          arr[j+1]=tmp;
        }
      }
    }
    
    int chongfuShu=0;
    int danshuchongfu=0;
    int[]arg=new int[arr.length];
    for(int m=0;m<arr.length;m++){
      for(int n=m+1;n<arr.length;n++){
        if(arr[m]==arg[n]){
          chongfushu++;
          danshuchongfu=m;
          m=m+1;
          continue;
        }
      }
     arg[m]=arr[m];
    }
  }
/*
求一个无序序列中第K大/小个数，如果没有重复元素，则直接排序，找到第K大个数就行，但是如果有重复的元素，就比较麻烦。没有搁进去的值，java会自动赋值0.
所以只能排序。
*/

4.回文字符串
方法1：
  public static void main(String[]args){
    String a="dfdfdf";
    int count=0;
    for(int i=0;i<a.length()/2;i++){
      if(a.substring(i,i+1).equals(s.substring(a.length()-1-i,a.length()-i)))
        count++;  
    }
    if(count==a.length()-1/2){
      System.out.println("是回文")；
    }else{
      System.out.println("不是回文")；
    }
  }
  方法2：
    stringBuilder中的reverse方法
5.进制转换
private static void test(){
    System.out.println("十转二："+Integer.toBinaryString(120));
    System.out.println("十转八："+Integer.toOctalString(120));
    System.out.println("十转十六："+Integer.toHexString(120));
    System.out.println("二转十："+Integer.valueOf("1010",2));
    System.out.println("八转十："+Integer.valueOf("125",8));
    System.out.println("十六转十："+Integer.valueOf("ABCDEF",16));
}


6.将四则运算规则变换为从左到右进行计算，就有+，-，*.
	Scanner cin=new Scanner(System.in);
		String a=cin.next();
		int sum = 0;
    //正则
    //正则表达式中想匹配*用想斜杠，或的话用|
    String[]arr1=a.replaceAll("[0-9]",",").split(",");
		String[]arr2=a.replaceAll("[+-]|\\*", ",").split(",");
		//想将一个string转换成int，Integer.valueOf(arr).intValue()
if(arr1[1].equals("+")){		
			sum=Integer.valueOf(arr2[0]).intValue()+Integer.valueOf(arr2[1]).intValue();
		
		}else if(arr1[1].equals("-")){
		
			sum=Integer.valueOf(arr2[0]).intValue()-Integer.valueOf(arr2[1]).intValue();
		
		}else if(arr1[1].equals("*")){
		
			sum=Integer.valueOf(arr2[0]).intValue()*Integer.valueOf(arr2[1]).intValue();
		
	}
    //用count控制运算。                                  
		int count=1;
                                      
		for(int i=2;i<arr2.length;i++){
			count++;
			if(count==arr1.length)
				break;
			if(arr1[count].equals("+")){	
					sum=sum+Integer.valueOf(arr2[i]).intValue();				
				}else if(arr1[count].equals("-")){				
					sum=sum-Integer.valueOf(arr2[i]).intValue();				
				}else if(arr1[count].equals("*")){				
					sum=sum*Integer.valueOf(arr2[i]).intValue();			
			}
		}
		System.out.println(sum);
		
		
