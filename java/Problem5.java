// Problem5.java --- 
// Filename: Problem5.java
// Description: 
// Author: amritendu
// Email:  amritoit@gmail.com
// Organization:  IIT Madras
// Created: Tue Mar  1 23:49:33 2016 (+0530)
// Last-Updated: Wed Mar  2 00:06:15 2016 (+0530)
//           By: amritendu
//     Update #: 27
// 

import java.util.Scanner;

public class Problem5{

    public static void main(String args[]){
        
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt();
        int N;

        while(T-->0){
            N=sc.nextInt();
            System.out.println(lcmOfOneTwoN(N));
        }
    }

    private static long lcmOfOneTwoN(int N){
        
        long lcdLast=1;
        for(int i=2;i<=N;i++){
            lcdLast=LCM(lcdLast,i);
        }
        return lcdLast;
    }

    private static long LCM(long a,long b){
        
        long gcd=GCD(a,b);
        return ( a * b ) / gcd;
    }

    /*Euler method to calculate the gcd of two number.*/
    private static long GCD(long a,long b){
        
        long temp;

        while (b != 0){
            temp = b;
            b = a % b; 
            a = temp; 
        }
        return a;
    }

    
}
