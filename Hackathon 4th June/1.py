# dynamic array implementation of stacks and queues 
# inbox and outbox stacks
import sys

n = int(sys.stdin.readline())

inbox = []
outbox = []
served = []

for _ in range(n):
    split = sys.stdin.readline().split()

    if split [0] == "ENQUEUE":
        inbox.append(split[1])

    elif split [0] == "DEQUEUE":
        
        if not outbox:
            while inbox:
                outbox.append(inbox.pop())

        if outbox:
            served.append(outbox.pop())


pending = len(inbox) + len(inbox)

print("Served = " ," ".join(served))
print("Pending = ",pending)