
a = [0, 1]


for i in range(20):
    a.append(a[-1] + a[-2])


for i in range(a):
    if a % 2 ==0:
        print a



# stack overflow

def fin(n):
    if n == 1 or n ==2:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(1, 10):
    print fib(i)
