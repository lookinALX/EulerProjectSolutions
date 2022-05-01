def find_evenly_divisible_number(n):
    for i in range(1, 10000000000):
        j = 1
        while i % j == 0:
            j += 1
            if j > n:
                return i


print(find_evenly_divisible_number(18))
