package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        int sum_even_fib = 0;
        int fib_number = 2;
        int i = 1;
        int j;
        while (fib_number < 4000000){
            if (fib_number % 2 == 0) {
                sum_even_fib +=fib_number;
            }
            j = fib_number;
            fib_number = fib_number + i;
            i = j;

        }
        System.out.println(sum_even_fib);
    }
}
