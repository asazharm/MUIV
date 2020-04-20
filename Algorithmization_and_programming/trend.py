import sys

numbers = sys.argv[1]

numbers = numbers.split(' ')
positive_trend = []
negative_trend = []

before = 0

for i in numbers:
    i = int(i)
    tmp = [i]
    for j in numbers:
        j = int(j)
        k = 1
        if j - i == k:
            tmp.append(j)
            k += 1
        else:
            continue
    if len(tmp) > 1:
        positive_trend.append(tmp)

for i in numbers:
    i = int(i)
    tmp = [i]
    for j in numbers:
        j = int(j)
        k = 1
        if i - j == k:
            tmp.append(j)
            k += 1
    if len(tmp) > 1:
        negative_trend.append(tmp)

print(positive_trend)
print(negative_trend)