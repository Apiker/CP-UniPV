"""Case study: letter frequency histogram"""

s = 'parrot'
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in l:
    c = s.count(i)
    if (c != 0):
        print(i + ":", c)