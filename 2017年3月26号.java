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
