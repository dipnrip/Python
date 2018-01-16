import sys
from fibo import fib, fib2

if __name__ == '__main__' :
    n = 50
    print("Fibonacci numbers up to ", n)
    fib(n)
    m = 30
    print("Fibonacci numbers up to ",  m,  " in a list")
    print(fib2(m))
