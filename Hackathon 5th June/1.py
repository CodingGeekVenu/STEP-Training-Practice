# fast track gate 

import sys
from collections import deque 

n = int(sys.stdin.readline())

boarded = []
quit = []
waiting = deque([])

for _ in range(n):
    line = list(sys.stdin.readline().split())
    if (line[0] == "REGULAR"):
        waiting.append(line[1])
    elif (line[0] == "VIP"):
        waiting.appendleft(line[1])
    elif (line[0] == "BOARD"):
        if waiting:
            x = waiting.popleft()
            boarded.append(x)
    elif (line[0] == "QUIT"):
        if waiting:
            y = waiting.pop()
            quit.append(y)

print("Boarded: ", " ".join(boarded))
print("Quit: ", " ".join(quit))
print("Waiting: ", " ".join(waiting))



