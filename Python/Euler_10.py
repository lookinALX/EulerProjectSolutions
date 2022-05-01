def erat(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n + 1, number):
                numbers[candidate - 2] = 0
    return numbers


def sum_primes_below_number(n):
    result = 0
    for i in erat(n):
        result += i
    return result


print(sum_primes_below_number(2000000))
