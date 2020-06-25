import math


def production_Pythagorean_triplet_digits(sum):
    """
    Takes a+b+c where a,b and c - Pythagorean_triplet_digits
    :return a*b*c
    """
    for a in range(1, 1000):
        b = a+1
        while a < b < 1000:
            c_sqr = a ** 2 + b ** 2
            if is_Pythagorean_triplet(c_sqr):
                if a + b + int(math.sqrt(c_sqr)) == sum:
                    return a * b * int(math.sqrt(c_sqr))
            b += 1


def is_Pythagorean_triplet(a_sqr_plus_b_sqr):
    if int(math.sqrt(a_sqr_plus_b_sqr)) ** 2 == a_sqr_plus_b_sqr:
        return True
    else:
        return False


print(production_Pythagorean_triplet_digits(1000))
