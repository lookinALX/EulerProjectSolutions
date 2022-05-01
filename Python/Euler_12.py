import math
from time import time

t = time()


def divisors(number):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(number))) + 1):
        if number % i == 0:
            number_of_factors += 2
        if i * i == number:
            number_of_factors -= 1
    return number_of_factors


for n in range(1, 10000000):
    tn = (n*(n+1))/2
    amount = divisors(tn)
    if amount >= 500:
        print(tn)
        break
tt = time() - t
print(tt)
