'''
10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

def CheckPrime(number):
    largest = int(number/2)
    prime = True
    for num in range(2, largest+1):
        if number % num == 0:
            prime = False
            break
    return prime

index = 10001
count = 0
number = 2
while(count < index):
    if(CheckPrime(number)):
        count += 1
    number += 1
print(number-1)
