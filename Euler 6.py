def summ_of_squares(n):
    summ = 0
    for i in range(n + 1):
        summ += i ** 2
    return summ


def square_of_sum(n):
    summ = 0
    for i in range(n + 1):
        summ += i
    return summ ** 2


print(square_of_sum(100) - summ_of_squares(100))
