def nested_sum(list):
    sum = 0
    for lists in list:
        for i in lists:
            sum += i
    print(sum)

t =  [[1, 2], [3], [4, 5, 6]]
nested_sum(t)