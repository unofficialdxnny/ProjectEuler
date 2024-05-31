'''
Largest Palindrome Product
Problem 4
'''

def is_palindrome(n):

  return str(n) == str(n)[::-1]

largest_palindrome = 0
for i in range(999, 100, -1):
  for j in range(999, i, -1):
    product = i * j
    if is_palindrome(product) and product > largest_palindrome:
      largest_palindrome = product

print(largest_palindrome)
