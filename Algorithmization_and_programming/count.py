import sys
symbols = ['', ' ', ',', '!', '?', '.', '-', ':']
sentence = sys.argv[1]
# print(sentence)
sentence = sentence.split(' ')
sentence = list(set(sentence))
# print(sentence)
sentence.sort()
# print(sentence)
for i in symbols:
    try:
        i
        sentence.remove(i)
        # print(i)
    except:
        continue
# print(sentence)
print(len(sentence))
