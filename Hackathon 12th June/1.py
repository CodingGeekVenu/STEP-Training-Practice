import sys

input_list = list(map(int, sys.stdin.readline().split()))

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# preorder = root left right
# inorder = left root right
# postorder = left right root

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

