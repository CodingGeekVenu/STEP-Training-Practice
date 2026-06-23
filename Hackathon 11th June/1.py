from collections import deque 
import sys

tokens = list(map(int, sys.stdin.readline().split()))

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def inorder(root, ans):
    inorder(root.left, ans)
    ans.append(root.val)
    inorder(root.right, ans)

ans = 