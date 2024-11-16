filename = 'assetts/words.txt'
histo = {}
fin = open(filename)

'''for line in fin:
    word = line.strip()
    wl = len(word)
    if (wl < len(histo)):
        histo[wl] +- 1
    else:
        num_zeros = wl - len(histo) + 1
        histo =+ [0] * num_zeros
        histo[wl] = 1
print(histo)'''

'''for line in fin:
    word = line.strip()
    wl = len(word)
    if (wl in histo):
        histo[wl].append(word)
    else:
        histo[wl] = histo.get(wl, []) + [word]
print(histo)'''

for line in fin:
    word = line.strip()
    wl = len(word)
    if (wl in histo):
        histo[wl].append(word)
    else:
        histo[wl] = histo.get(wl, []) + [word]