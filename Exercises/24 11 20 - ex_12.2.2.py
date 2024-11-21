db = {}

path = 'assets/words.txt'
file = open(path)

for line in file:
    word = line.strip().lower()
    key = ''.join(sorted(list(word)))

    if key not in db:
        db[key] = [word]
    else:
        db[key].append(word)

anagramList = []
for key in db:
    if len(db[key]) > 1:
        anagramList.append((len(db[key]), db[key]))

anagramList.sort(reverse=True)
for record in anagramList:
    print(record)

print("\n BINGO LIST \n")

bingoList = []
for key in db:
    if len(key) == 8:
        if len(db[key]) > 1:
            bingoList.append((len(db[key]), db[key]))

bingoList.sort()
for record in bingoList:
    print(record)