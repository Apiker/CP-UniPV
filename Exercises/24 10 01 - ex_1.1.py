"""Think Python 2 - exercise 1.1"""

# normal print() statement
print('Normal print() statement: print("Hello, world!")')
print("Output: Hello, World!")

# one or both parentheses open
print('print "Hello, World!"')
print("Output: SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?")

# positive of negative number
print(">>> +-2")
print("Output: -2")

# double plus sign
print(">>> 2++2")
print("Output: 4")

# leading zeros
print(">>> 09")
print("Output: SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers")
print(">>> 011")
print("Output: SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers")

# no operator

print(">>> 1 2")
print("Output: SyntaxError: incomplete input")
print(">>> 12")
print("Output: 12")