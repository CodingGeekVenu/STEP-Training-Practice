# min price tracker 

import sys

n = int(sys.stdin.readline())

stack =[]
mins = []

for _ in range(n):
    split = sys.stdin.readline().split()

    if split[0] == "MIN":
        if not mins:
            print("Min : Empty")
        else:
            print("Min : ",mins[-1])
    
    elif split[0] == "POP":
        if stack and mins:
            stack.pop()
            mins.pop()
    elif split[0] == "PUSH":
        if not mins:
            stack.append(int(split[1]))
            mins.append(int(split[1]))
        else:
            stack.append(int(split[1]))
            mins.append(min(int(split[1]),mins[-1]))


print("Size", len(stack))
