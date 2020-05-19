'''
Sum square difference
The sum of the squares of the first ten natural numbers is 385
The square of the sum of the first ten natural numbers is 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
maximum = 100
squares_sum = sum([pow(x, 2) for x in range(1, maximum+1)])
sum_squared = pow(sum([x for x in range(1, maximum+1)]), 2)
print(abs(squares_sum - sum_squared))
