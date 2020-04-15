import sys
import collections

word = sys.argv[1]
word = word
word_list = []

for i in word:
    word_list.append(i)

word_list.sort()
# print(word_list)
# word_sort = set(word_list)
# print(word_sort)
word_list = collections.OrderedDict.fromkeys(word_list).keys()
word_sort = ''.join(word_list)
print(word_sort)
