""" 
The miller_rabin function performs the Miller-Rabin primality test on the input number n.
It first checks if n is 2 or 3 (which are prime), or if n is less than 2 or even (which means it's not prime).
It then writes n - 1 as 2^r * d, where d is odd.
It performs the test k times. For each test, it picks a random integer a between 2 and n - 1, and computes a^d mod n. If this is 1 or n - 1, it continues to the next test.
If a^d mod n is not 1 or n - 1, it squares a^d mod n r - 1 times and checks if the result is n - 1. If it is, it continues to the next test. If it's not, it returns False (meaning n is composite).
If n passes all k tests, it returns True (meaning n is probably prime).,
"""

import random

def miller_rabin(n, k=5):  # number of tests to run
    if n == 2 or n == 3:
        return True

    if n <= 1 or n % 2 == 0:
        return False

    # write (n - 1) as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # witness loop
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Test the function
print(miller_rabin(561))  # False
print(miller_rabin(563))  # True