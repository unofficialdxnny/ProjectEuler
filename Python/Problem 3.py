def is_prime(num):
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def prime_factorization(num):
  if num <= 1:
    return []
  prime_factors = []
  while num % 2 == 0:
    prime_factors.append(2)
    num //= 2
  i = 3
  while i * i <= num:
    if num % i == 0:
      prime_factors.append(i)
      while num % i == 0:
        num //= i
    i += 2
  if num > 1:
    prime_factors.append(num)
  return prime_factors

# Example usage
number = 600851475143
prime_factors = prime_factorization(number)

if prime_factors:
  print(f"Prime factorization of {number} is: {prime_factors}")
else:
  print(f"{number} is a prime number")
