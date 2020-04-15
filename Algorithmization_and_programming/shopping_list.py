sl1 = open('shopping_list_1.txt', encoding='UTF-8')
sl1 = sl1.read()
sl2 = open('shopping_list_2.txt', encoding='UTF-8')
sl2 = sl2.read()
sl3 = open('shopping_list_3.txt', encoding='UTF-8')
sl3 = sl3.read()

all_sl = sl1 + sl2 + sl3
all_sl = all_sl.split('\n')
all_sl = list(set(all_sl))
all_sl.sort()
all_sl = '\n'.join(all_sl)
# print(all_sl)

all_slf = open('shopping_list.txt', 'w', encoding='UTF-8')
all_slf.write(all_sl)