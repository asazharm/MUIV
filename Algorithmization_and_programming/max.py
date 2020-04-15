import sys

numbers = sys.argv[1:6]
for i in numbers:
    index = numbers.index(i)
    i = int(i)
    numbers[index] = i
numbers.sort()
print(numbers[-1])