def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib2  = lambda n: n if n < 2 else fib(n-1) + fib(n-2)    

fibreq = 4

print(fib(fibreq))
print(fib2(fibreq))
