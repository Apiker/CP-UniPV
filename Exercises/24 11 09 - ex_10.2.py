def cumsum(list):
    sum = []
    x = 0
    for i in list:
        c = x + i
        sum.append(c)
        x = c
    print(sum)

t = [1, 2, 3]
cumsum(t)

