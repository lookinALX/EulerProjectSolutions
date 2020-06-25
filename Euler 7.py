def sieve_of_eratosthenes(n: int):
    """ Take the number n
        :return the list of True for prime and False for else
    """
    new_list = []
    prime_list = [True] * n
    prime_list[0] = prime_list[1] = False
    for k in range(2, n):
        if prime_list[k]:
            for m in range(2 * k, n, k):
                prime_list[m] = False
    for k in range(n):
        if prime_list[k]:
            new_list.append(k)
    print(new_list[100000])

# FIXME
def generate_nst_prime(n: int):
    prime_list = []
    number_list = [True] * 200
    number_list[0] = number_list[1] = False
    i = 1
    j = 1
    while len(prime_list) <= n:
        for k in range(2 * i, 200 * j):
            if number_list[k]:
                for m in range(2 * k, 200 * j, k):
                    number_list[m] = False
        for k in range(i, 200 * j):
            if number_list[k]:
                prime_list.append(k)
        for k in range(200):
            number_list.append(True)
        i = 100 * j
        j += 1
    print(prime_list[n - 1])


def erat_sieve(bound):
    if bound < 2:
        return []
    max_ndx = (bound - 1) // 2
    sieve = [True] * (max_ndx + 1)
    #loop up to square root
    for ndx in range(int(bound ** 0.5) // 2):
        # check for prime
        if sieve[ndx]:
            # unmark all odd multiples of the prime
            num = ndx * 2 + 3
            sieve[ndx+num:max_ndx:num] = [False] * ((max_ndx-ndx-num-1)//num + 1)
    # translate into numbers
    return [2] + [ndx * 2 + 3 for ndx in range(max_ndx) if sieve[ndx]]


print(erat_sieve(100000000)[10000])