import math



def get_num_of_digits(num):
    if num < 10:
        return 1
    else:
        return 1 + get_num_of_digits(num / 10)


def is_palindrome(num):
    num_of_digits = get_num_of_digits(num)
    for i in range(1, math.floor(num_of_digits / 2) + 1):
        left_digit = math.floor(num / (10 ** (num_of_digits - i))) % 10
        right_digit = math.floor((num % (10 ** i)) / (10 ** (i - 1)))
        if left_digit != right_digit:
            return False
    return True


def find_largest():
    largest = -1

    for i in range(999, 99, -1):
        for j in range(999, i - 1, -1):
            num = i * j

            if (j == 999) and (num < largest):
                return largest

            if (num > largest) and is_palindrome(num):
                largest = num

    return largest


print(find_largest())

