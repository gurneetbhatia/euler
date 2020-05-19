'''
Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

def sieve(n):
    prime = [True] * n
    prime[0] = False
    prime[1] = False

    p = 2
    while(p*p <= n):
        if(prime[p]):
            for i in range(2*p, n, p):
                prime[i] = False
        p += 1
    return prime

def primeSummation(n):
    prime = sieve(n)
    total = 0
    for (index, value) in enumerate(prime):
        if value:
            total += index
    return total

print(primeSummation(2000000))
