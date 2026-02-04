def fibosum(n):
    a = 0
    b = 1
    i = 1
    res = 1
    if n == 1:
        res = a
    elif n == 2:
        res = b
    else:
        while i < n:
            c = a + b
            res += c
            a = b
            b = c
            i += 1
    return res

print("The sum of the first 5 terms is:", fibosum(5))
print("The sum of the first 10 terms is:", fibosum(10))