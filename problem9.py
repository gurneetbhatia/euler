'''
Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
(a^2) + (b^2) = (c^2)
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

total = 1000
for a in range(1, total):
    found = False
    for b in range(1, total):
        c = total - a - b
        if(pow(a, 2) + pow(b, 2) == pow(c, 2)):
            found = True
            print(a,b,c)
            print(a * b * c)
            break
    if found:
        break
