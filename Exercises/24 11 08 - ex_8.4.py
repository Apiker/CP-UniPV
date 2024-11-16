# CORRECT
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# WRONG
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
        
# WRONG
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# WRONG
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# WRONG
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False #!!!
    return True

c = str("Nel mezzo del cammin di nostra vita mi ritrovi per una selva oscura che la diritta via era smarrita")
g = str("nel mezzo del cammin di nostra vita mi ritrovi per una selva oscura che la diritta via era smarrita")

print(any_lowercase5(c))
print(any_lowercase5(g))