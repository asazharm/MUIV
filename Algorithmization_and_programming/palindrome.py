import sys

arg = str(sys.argv[1])
arg_reverse = arg[::-1]
if arg == arg_reverse:
    print(1)
else:
    print(0)