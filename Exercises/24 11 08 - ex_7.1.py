import math

# input function
def userinput(n):
    l = []
    for i in range(n):
        a = float(input("Write any number: "))
        l.append(a)
    return l

# Newton's square root
def mysqrt(a):
    precision = .0001
    x = a
    root = 2*x+precision
    while abs(x-root) >= precision:
        x = root
        root = (x + a/x)/2
        #print(x, y, math.sqrt(a))
    return root

# string formatting for the table
def formatting_str(s, field):
    str = ' '*(field-len(s))+s
    return str


n = int(input("Write number of items: "))
list = userinput(n)

# table header
# just to look fancy and professional
a_field = 3
mysqrt_field = 20
sqrt_field = 20
diff_field = 21

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

# populate table
for i in range(n):
    a = list[i]
    root = mysqrt(a)
    sqrt_a = math.sqrt(a)
    diff = abs(root - sqrt_a)
    print(
        formatting_str(str(a), a_field),
        formatting_str(str(root), mysqrt_field),
        formatting_str(str(sqrt_a), sqrt_field),
        formatting_str(str(diff), diff_field)
    )