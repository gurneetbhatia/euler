'''
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29
What is the largest prime factor of the number 600851475143?
'''
def GetPrimeFactors(number):
    p = 2
    while(number >= p * p):
        if(number % p == 0):
            number = number/p
        else:
            p += 1
    return int(number)

print(GetPrimeFactors(600851475143))
