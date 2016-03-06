// Problem3.java --- 
// Filename: Problem3.java
// Description: 
// Author: amritendu
// Email:  amritoit@gmail.com
// Organization:  IIT Madras
// Created: Sun Feb 28 10:00:37 2016 (+0530)
// Last-Updated: Sun Feb 28 10:37:25 2016 (+0530)
//           By: amritendu
//     Update #: 32
// 

public class Problem3{

    public static void main(String[] args){
        
        if(args[0]==null)System.out.println("Please pass the number to me: java <className> <number> ");
        System.out.println(greatestPrimeFactor(Long.parseLong(args[0])));
   
    }

    private static long greatestPrimeFactor(long n){
        
        int limit=(int)Math.sqrt(n)+1;
        int i=3;

        if(n==4)return 2;
        if(n==1)return 0;

        for(i=3;i<=limit;i=i+2){
            
            while(isEven(n)){
                n=n/2;
                if(n==1)return 2;
            }


            while(n%i==0)
                 n=n/i;

            if(n==1)break;
        }
        
        if(n==1)return i;
        else return n;
        
    }

    private static boolean isEven(long n){
        
        return (n & 1)==1?false:true;
    }
}
