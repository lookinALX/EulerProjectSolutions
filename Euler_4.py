def is_it_palindromic(number):
    """
    Function checks is the number palindromic
    :param number: int
    :return: True and number
    """
    check_number = list(str(number))
    l = len(check_number)
    k = -1
    # Если количество цифр четное
    if len(check_number) % 2 == 0:
        for i in range(len(check_number[l // 2: l]) - 1):
            check_number[k], check_number[i + l // 2] = check_number[i + l // 2], check_number[k]
            k -= 1
        if check_number[:l // 2] == check_number[l // 2: l]:
            return True
    # Если количество цифр нечетное
    else:
        for i in range(len(check_number[l // 2 + 1: l]) - 1):
            check_number[k], check_number[i + l // 2 + 1] = check_number[i + l // 2 + 1], check_number[k]
            k -= 1
        if check_number[:l // 2] == check_number[l // 2 + 1: l]:
            return True


def generate_numbers():
    k = 0
    for i in range(100, 999):
        for j in range(100, 999):
            if is_it_palindromic(i * j):
                if i*j > k:
                    k = i*j
    print(k)


generate_numbers()
