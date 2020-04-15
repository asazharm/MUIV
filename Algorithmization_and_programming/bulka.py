import sys

list = sys.argv[1]

list = list.split(',')
# list.insert(-1, 'и')
new_list = ', '.join(list[:-1])
list = '{} и {}.'.format(new_list, list[-1]).capitalize()
print(list)
