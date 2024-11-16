t = [1, 2, 3]
s = 'ABC'

def global2():
    #print('b', t, s) this will give an error (s called before assignment)
    s = 'xyz'
    print('c', t, s)

print('a', t, s)
global2()
print('d', t , s)