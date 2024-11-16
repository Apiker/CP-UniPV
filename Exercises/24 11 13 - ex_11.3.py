cache = {}

def ackermann(m ,n):
    if (m == 0):
        r = n+1
        return r
    if (m > 0) and (n == 0):
        r = ackermann(m - 1,1)
        return r
    else:
        r = ackermann(m - 1, ackermann(m, n - 1))
        return r
    
def ackermannmem(m ,n):
    if (m == 0):
        r = n+1
        return r
    if (n == 0):
        r = ackermann(m - 1,1)
        return r
    
    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]
    
print(ackermann(3, 4))
print(ackermannmem(4, 5))