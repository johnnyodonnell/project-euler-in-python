
primes = [2]

def is_prime(num):
    for prime in primes:
        if (i % prime) == 0:
            return False
    return True


i = 3

while (len(primes) < 10001):
    if is_prime(i):
        primes.append(i)
    i += 2

print(primes[-1])

