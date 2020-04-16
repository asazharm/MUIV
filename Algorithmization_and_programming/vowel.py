import sys
word = sys.argv[1]
words_vowels = ''
VOWELS = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y')

for i in word:
    if i in VOWELS:
        words_vowels += i
    else:
        continue

print(words_vowels)