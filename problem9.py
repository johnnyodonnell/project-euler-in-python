import math


sum_ = 1000

for a in range(1, math.ceil(sum_ / 3)):
    for b in range(a + 1, math.ceil((sum_ - a) / 2)):
        c = sum_ - (a + b)
        if ((a ** 2) + (b ** 2)) == (c ** 2):
            print(a * b * c)
            exit()

