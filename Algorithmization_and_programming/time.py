import sys
# import time
seconds = int(sys.argv[1])

if seconds < 60:
    if seconds < 10:
        seconds = '0' + str(seconds)
    print(seconds)
elif seconds < 3600:
    minutes = seconds // 60
    if minutes < 10:
        minutes = '0' + str(minutes)
    seconds = seconds % 60
    if seconds < 10:
        seconds = '0' + str(seconds)
    print('{}:{}'.format(minutes, seconds))
elif seconds < 86400:
    hours = seconds // 3600
    if hours < 10:
        hours = '0' + str(hours)
    minutes = (seconds % 3600) // 60
    if minutes < 10:
        minutes = '0' + str(minutes)
    seconds = (seconds % 3600) % 60
    if seconds < 10:
        seconds = '0' + str(seconds)
    print('{}:{}:{}'.format(hours, minutes, seconds))