'''
Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

palindrome = lambda s: s == s[::-1]
palindromes = []
for num1 in range(999, 99, -1):
    answer = None
    for num2 in range(999, num1-1, -1):
        product = num1*num2
        if(palindrome(str(product))):
            palindromes.append(product)
            break
print(max(palindromes))
