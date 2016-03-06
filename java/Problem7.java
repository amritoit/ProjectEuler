// Problem7.java --- 
// Filename: Problem7.java
// Description: 
// Author: amritendu
// Email:  amritoit@gmail.com
// Organization:  IIT Madras
// Created: Wed Mar  2 00:20:11 2016 (+0530)
// Last-Updated: Wed Mar  2 00:50:23 2016 (+0530)
//           By: amritendu
//     Update #: 21
// 

import java.util.Scanner;

public class Problem7{
    
    public static void main(String [] args){

        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt();
        int N;
        int cachelastIndex=1;
        int cache[]=new int[1000000];
        cache[0]=2;
        cache[1]=3;
        

        while(T-->0){
            N=sc.nextInt();
            if(N-1>cachelastIndex){
                System.out.println(returnNthPrime(N,cache,cachelastIndex));
                cachelastIndex=N-1;
            }
            else
                System.out.println(cache[N-1]);
        }
    }

    private static int returnNthPrime(int n,int cache[],int cachelastIndex){
        
        for(int i=cache[cachelastIndex]+2;;i+=2){
            if(n==cachelastIndex+1)return i-2;

            for(int j=cachelastIndex;j>=0;j--){
                if(i%cache[j]==0)break;
                if(j==0){
                    cachelastIndex+=1;
                    cache[cachelastIndex]=i;
                }
            }
        }

    }
}
