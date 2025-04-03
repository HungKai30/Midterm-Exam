import math

def is_prime(n):

  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True


n = int(input("Type n "))

# Kiểm tra và in kết quả
if is_prime(n):
  print(n, "is a prime number")
else:
  print(n, "not a prime number")