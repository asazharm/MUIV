import sys

value = sys.argv[1]
value = value.split(' ')
old_value = 0
sq = False
for i in value:
    i = int(i)
    if i > old_value:
        old_value = i
        sq = True
    else:
        print(0)
        sq = False
        break

if sq:
    print(1)