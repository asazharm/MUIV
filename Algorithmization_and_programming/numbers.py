with open('numbers.txt', 'r', encoding='UTF-8') as f:
    numbers = f.read()
    numbers = numbers.split(' ')
    sum = 0
    for i in numbers:
        i = int(i)
        if i < 0:
            sum += i
    print(sum)