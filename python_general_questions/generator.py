# Normal function

#  0,1,1,2,3,5

def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a+b


print(fibo(5))


def fibo_with_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


fib = fibo_with_generator(5)


for i in range(5):
    print(fib.__next__())
