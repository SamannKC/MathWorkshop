# length = 10
# width = 5
# area = length * width
# print(area)

def fib(n):
  a, b = 0 , 1
  for _ in range(n):
    a , b = b , a + b
    print(a, end = " ")

def SumDigits(n):
  if n == 0:
    return 0

  return n % 10 + SumDigits(n // 10)

def squaredSum(arr):
  sum = 0
  for i in range(len(arr)):
    sum += arr[i] * arr[i]
  print(sum)

def sumDigits(n):
  if n == 0:
    return 0
  return n + sumDigits(n - 1)
