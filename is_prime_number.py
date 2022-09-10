import time
import math

#------version-1------

def is_prime_v1(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#------version-2------

def is_prime_v2(n):
    if n == 1:
        return False
    max_di = math.floor((math.sqrt(n)))
    for i in range(2, 1 + max_di):
        if n % i == 0:
            return False
    return True

#------version-3------

def is_prime_v3(n):
    if n == 2:
        return True
    if n == 1:
        return False
    max_di = math.floor((math.sqrt(n)))
    for i in range(3, 1 + max_di, 2):
        if n % i == 0:
            return False
    return True

#------version-4------

def is_prime_v4(n):
    if n % 2 == 0:
        return False
    if n == 1:
        return False
    max_di = math.floor((math.sqrt(n)))
    for i in range(2, 1 + max_di):
        if n % i == 0:
            return False
    return True

#------time takes to run------

t1 = time.time()
for i in range(1, 100001):
    is_prime_v4(i)
t2 = time.time()
print(t2 - t1)