
sum_of_squares = 0
sum_ = 0

for i in range(1, 101):
    sum_ += i
    sum_of_squares += i ** 2

print((sum_ ** 2) - sum_of_squares)

