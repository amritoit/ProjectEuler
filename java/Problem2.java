// Problem2.java --- 
// Filename: Problem2.java
// Description: 
// Author: amritendu
// Email:  amritoit@gmail.com
// Organization:  IIT Madras
// Created: Sat Feb 27 14:51:21 2016 (+0530)
// Last-Updated: Sat Feb 27 15:07:10 2016 (+0530)
//           By: amritendu
//     Update #: 25
// 

public class Problem2{

    public static void main(String[] args){
        
        if(args[0]==null)System.out.println("Please pass the number to me: java <className> <number> ");
        int n=Integer.parseInt(args[0]);
        System.out.println(calEvenNumSumFromFibonacciSeries(n));
    }
    
    private static int calEvenNumSumFromFibonacciSeries(int MaxNo){
        
        int l=1,r=1,sum=0;
        
        for(;;){
            r=l+r;
            l=r-l;
            if(r>=MaxNo)break;
            if(r%2==0)sum+=r;
        }

        return sum;
    }

    private static void swap(int a, int b){
        a=a+b;
        b=a-b;
        a=a-b;
    }
}
