t = [1, 2, 3]
s = 'ABC'

def global1():
    print('b', t, s)
    t[1] = 0
    print('c', t, s)

print('a', t, s)
global1()
print('d', t , s)