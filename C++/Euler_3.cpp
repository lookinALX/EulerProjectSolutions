//
//  main.cpp
//  somePractice
//
//  Created by Alexander Lukin on 22.04.2021.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    // insert code here...
    long number;
    long number1;
    bool flag = true;
    std::cin >> number;
    number1 = sqrt(number);
    
    if (number % 2 != 0) {
        for (int i = 3; i <= number1; i += 2) {
            if (number % i == 0) {
                number = number / i;
                for (int j = 3; j<i; j+=2) {
                    if (i % j == 0){
                        flag = false;
                        break;
                    }
                }
                if (flag == true) {
                    std::cout << i << '\n';
                }
            }
        }
    }
    else {
        for (int i = 2; i <= number1; i += 1) {
            if (number % i == 0) {
                number = number / i;
                for (int j = 2; j<i; j+=1) {
                    if (i % j == 0){
                        flag = false;
                        break;
                    }
                }
                if (flag == true) {
                    std::cout << i << '\n';
                }
            }
        }
    }
    
    for (int j = 2; j < number; j += 1) {
        if (number % j == 0){
            break;
        }
        else{
            std::cout << number <<'\n';
        }
    }
    return 0;
}
