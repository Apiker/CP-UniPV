"""Case study: letter frequency histogram"""

s = input("Write a word: ")

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def print_hist(h):
    for c in h:
        print(c + ":", h[c])


print_hist(histogram(s))