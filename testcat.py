part1 = "Miao"
part2 = "Bau"
part3 = "Quack"

def print_twice(var):
    print(var)
    print(var)

def cat_twice(pippo, paolo):
    cat = pippo + paolo
    print_twice(cat)

cat_twice(part1, part2)