
def get_greatest_common_divisor(num1, num2):
    greatest = 1
    for i in range(2, min(num1, num2) + 1):
        if ((num1 % i) == 0) and ((num2 % i) == 0):
            greatest = i
    return greatest


num = 1

for i in range(20, 0, -1):
    if (num % i) != 0:
        gcd = get_greatest_common_divisor(num, i)
        num *= (i / gcd)

print(num)

