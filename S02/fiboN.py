
def fibon(n):
    a = 0
    b = 1
    i = 1
    if n == 1:
        c = a
    elif n == 2:
        c = b
    else:
        while i < n:
            c = a + b
            a = b
            b = c
            i += 1
    return c

print("The 5th Fibonacci number is:", fibon(5))
print("The 10th Fibonacci number is:", fibon(10))
print("The 15th Fibonacci number is:", fibon(15))


