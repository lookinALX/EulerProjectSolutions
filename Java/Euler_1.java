package com.company;

public class Main {

    public static void main(String[] args) {
        int sum = 0;

        for (int i = 1; 3*i < 1000; i++) {
            sum = sum + 3*i;
            if ((5*i % 3*i != 0) && (5*i < 1000)){
                    sum = sum + 5*i;
            }
        }
        System.out.println(sum);
    }
}
