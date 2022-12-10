
largest = 1
# num = 13195
num = 600851475143
i = 2

while(num > 1):
    while(i <= num):
        if ((num % i) == 0):
            largest = i
            num = (num / i)
            break
        i += 1

print(largest)

