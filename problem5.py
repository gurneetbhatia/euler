'''
Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
from functools import reduce

def Check(number):
    divisible = True
    for x in range(2, 21):
        if number % x != 0:
            divisible = False
            break
    return divisible

largest = reduce(lambda a, b: a * b, [x for x in range(2, 21)])
print(largest)
smallest = 10
while(smallest > 1):
    print(largest,'/',smallest,'=',(largest/smallest))
    if(largest%smallest == 0 and Check(largest/smallest)):
        largest = int(largest / smallest)
    else:
        smallest -= 1

print(largest)
