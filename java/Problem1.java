// 1.java --- 
// Filename: 1.java
// Description: 
// Author: amritendu
// Email:  amritoit@gmail.com
// Organization:  IIT Madras
// Created: Sat Feb 27 11:58:58 2016 (+0530)
// Last-Updated: Sat Feb 27 23:25:48 2016 (+0530)
//           By: amritendu
//     Update #: 19
// 

public class Problem1{


    public static void main(String[] args){
        
        if(args[0]==null)System.out.println("Please pass the number to me: java <className> <number> ");
        System.out.println(calSum(Integer.parseInt(args[0])-1));
    }

    private static int calSum(int n){
        
        int mulOf3=n/3;
        int mulOf5=n/5;
        int mulOf15=n/15;
        
        int sumOf3=3*(mulOf3*(mulOf3+1))>>1;
        int sumOf5=5*(mulOf5*(mulOf5+1))>>1;
        int sumOf15=15*(mulOf15*(mulOf15+1))>>!;
        
        return sumOf3+sumOf5-sumOf15;

    }

}
