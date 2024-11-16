import math

'''while True:
    y = (x + a/x)/2
    if abs(x-y) > precision:
        print(x, y, math.sqrt(a))
        x = y
    else:
        break

y = 2*x+precision

while abs(x-y) <= precision:
    x = yy = (x + a/x)/2
    #print(x, y, math.sqrt(a))'''

def mysqrt(a):
    precision = .001
    x = 100
    y = 2*x+precision
    while abs(x-y) >= precision:
        x = y
        y = (x + a/x)/2
        #print(x, y, math.sqrt(a))
    return y

def formatting_str(s, field):
    str = ' '*(field-len(s))+s
    return str

#a = 121


#y = mysqrt(a)
#precision = .001
#x = 100

a_field = 3
mysqrt_field = 20
sqrt_field = 20
diff_field = 20

# HEADER
a_header = 'a'
a_str = formatting_str(a_header, a_field)
mysqrt_header = 'mysqrt(a)'
mysqrt_str = formatting_str(mysqrt_header, mysqrt_field)
sqrt_header = 'sqrt(a)'
sqrt_str = formatting_str(sqrt_header, sqrt_field)
diff_header = 'diff'
diff_str = formatting_str(diff_header, diff_field)

print(a_str, mysqrt_str, sqrt_str, diff_str)
print('-'*a_field, '-'*mysqrt_field, '-'*sqrt_field, '-'*diff_field)




#print('sqrt(', a, '): ', y)

for a in range(1,10):
    y = mysqrt(a)
    sqrt_a = math.sqrt(a)
    diff = abs(y - sqrt_a)
    print(
        formatting_str(str(a), a_field),
        formatting_str(str(y), mysqrt_field),
        formatting_str(str(sqrt_a), sqrt_field),
        formatting_str(str(diff), diff_field)
    )
    #print('sqrt(', a, '): ', y, '|', math.sqrt(a), '|', abs(y-math.sqrt(a)))