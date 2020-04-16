import sys

first_day = int(sys.argv[1])
day = int(sys.argv[2])

if 0 < day < 367:
    if day > first_day:
        day -= first_day
        day //= 7
        print(day + 1)
    elif day == first_day:
        print(1)
    elif day < first_day:
        print(-1)
else:
    print(-1)