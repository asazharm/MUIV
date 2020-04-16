import sys

N = int(sys.argv[1])
M = int(sys.argv[2])
L = int(sys.argv[3])
T = int(sys.argv[4])

sum = N + M + L
value = T % sum

if value < N:
    print('green')
elif value < N + M:
    print('yellow')
elif value < N + M + L:
    print('red')