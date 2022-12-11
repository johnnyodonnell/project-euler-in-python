
# limit = 10
limit = 2000000
primes = [2]

def is_prime(num):
    for prime in primes:
        if (prime ** 2) > num:
            return True
        elif (i % prime) == 0:
            return False
    return True


i = 3

while(primes[-1] < limit):
    if is_prime(i):
        primes.append(i)
    i += 2

print(sum(primes[:-1]))

