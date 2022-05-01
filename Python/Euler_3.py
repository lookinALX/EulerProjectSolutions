def find_max_prime_factor(number):
    factor = 2
    last_factor = 1
    while number > 1:
        if number % factor == 0:
            last_factor = factor
            number //= factor
            while number % factor == 0:
                number //= factor
        factor += 1
    return last_factor


print(find_max_prime_factor(600851475143))
print(find_max_prime_factor(129))
