import sys

ages = sys.argv[1]
ages = ages.split(' ')
ages2 = ages[:]
index = 0

for i in ages:
    ages[index] = int(i)
    index += 1

ages.sort()
ages2.pop(ages2.index(str(ages[-1])))
ages2.insert(0, str(ages[-1]))

ages2 = ' '.join(ages2)
print(ages2)
