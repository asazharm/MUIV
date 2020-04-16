with open('matrix.txt', 'r', encoding='UTF-8') as f:
    index = 0
    sum = 0
    matrix = f.readlines()
    for i in matrix:
        i = i.split(' ')
        i = int(i[index])
        sum += i
        index += 1

    print(sum)
    # print(len(matrix))