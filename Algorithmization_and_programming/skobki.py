import sys

value = sys.argv[1]

open_skob = value.count('(')
close_skob = value.count(')')

if open_skob == close_skob and value.index('(') < value.index(')'):
    print(1)
else:
    print(0)