def middle(list):
    mid = []
    for i in range(len(list)-2):
        i += 1
        mid.append(list[i]) 
    print(mid)

t = [1, 2, 3, 4]
middle(t)