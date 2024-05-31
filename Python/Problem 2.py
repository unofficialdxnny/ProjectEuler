'''
Even Fibonacci Numbers
Problem 2

'''

def is_even(num):
  return num % 2 == 0

def fibonacci_iterative(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a + b
  return a

n = 1
sum = 0
while fibonacci_iterative(n) <= 4000000:
  if is_even(fibonacci_iterative(n)):
    sum += fibonacci_iterative(n)
  n += 1

print(sum)
