def find_multiples(num, stop):
    """Take a number and stop point. Gives multiples of number below stop point"""
    s = []
    for x in range(stop):
        if x % num == 0 and x != 0:
            s.append(x)
    return s


def kill_duplicates(l1, l2):
    """Take two lists. Save a list without duplicates"""
    return list(set(l1 + l2))


def summarizer(l1):
    s = 0
    for i in range(len(l1)):
        s += l1[i]
    return s


def correct_solve(num1, num2, stop):
    """Takes two int and range. Gives sum of multiples of numbers below stop point"""
    result = 0
    for x in range(stop):
        if (x % num1 == 0 and x != 0) or (x % num2 == 0 and x != 0):
            result += x
    return result


r1 = find_multiples(3, 1000)
r2 = find_multiples(5, 1000)

print(kill_duplicates(r2, r1))

print(summarizer(kill_duplicates(r2, r1)))

print(correct_solve(3, 5, 1000))