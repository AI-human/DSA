

n = int(input())
ans = 1
for i in range(n,1,-1):
  ans *= i

# print(ans)

def headRecursion(n):
  if n>0:
    headRecursion(n-1)# head recursion
    print(n) 
# headRecursion(n)

def tailrecursion(n):
  if n>0:
    print(n) 
    tailrecursion(n-1) # tail recursion
# tailrecursion(n)

def factorial(n):
  if n==1:
    return n
  return n*factorial(n-1)
# print(factorial(n))


def fib_recursive(n):
  if n<=1:
    return n
  return fib(n-1)+fib(n-2)

# print(fib(n))


def fib_iterative(n: int) -> int:
    Sum = [0,1]
    for i in range(2,n+1):
        Sum.append(Sum[i-1]+ Sum[i-2])
    return Sum[n]

print(fib_iterative(n))

# 1D dp

def fib(n,cache):
  if n<=1:
    return n
  if n in cache:
    return cache[n]
  
  cache[n] = fib(n-1,cache)+fib(n-2,cache)
  return cache[n]

# print(fib(n,{}))

