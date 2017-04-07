1.最大公约数与最小公倍数：解法：用辗转相除法先求出最大公约数，再通过公式：两个数相乘等于这两个数的最大公约数和最小公倍数的积。求出最小公倍数
    public static int commonDivisor(int n,int m){
    //辗转相除是用大的除以小的。如果n<m，第一次相当n与m值交换
    while(n%m!=0){
    int temp=n%m;
    n=m;
    m=temp;
    }
    return m;
    }
    //求最小公倍数
    public static int commonMultiple(int n,int m){
    return n*m/commonDivisor(n,m);
    }
    
 2.反转整数：有个坑点，就是要考虑负数
    public class Solution {
    /**
     * @param n the integer to be reversed
     * @return the reversed integer
     */
    public int reverseInteger(int n) {
       String s=String.valueOf(n);
       StringBuffer sb=new StringBuffer(s);
		sb=sb.reverse();
		String a=sb.toString();
		return Integer.valueOf(a);
    }
}
3.斐波那契数列
4.质因数
5.丑数字
6.二叉树的前序遍历
7二叉树的后序遍历
8.二叉树的中序遍历
