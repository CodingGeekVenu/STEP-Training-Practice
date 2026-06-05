# min price montior 

import sys

line1 = sys.stdin.readline().split()
n = int(line1[0])
k = int(line1[1])

num = list(sys.stdin.readline().split())

Maxima =[]

for i in range (n -k +1):
    window = num[i:i+k]
    Maxima.append(max(window))

print("Window Maxima: ", " ".join(Maxima))
