

def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)


res = [fib(i) for i in range(1, 21)]
print(res)


def fib_loop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


for i in range(20):
    print(fib_loop(i), end=', ')

