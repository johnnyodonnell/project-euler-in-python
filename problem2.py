
final_sum = 0

fib_num_1 = 1
fib_num_2 = 1

while (fib_num_2 < 4000000):
    if (fib_num_2 % 2) == 0:
        final_sum += fib_num_2

    tmp = fib_num_2
    fib_num_2 = fib_num_1 + fib_num_2
    fib_num_1 = tmp

print(final_sum)


