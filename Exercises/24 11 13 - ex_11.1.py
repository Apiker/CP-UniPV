data = dict()

text = open('assets/words.txt')

for line in text:
    word = line.strip()
    data[word] = '|'

print(data)