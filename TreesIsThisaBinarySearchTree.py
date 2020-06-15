""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    x = []
    l = []

    def check(root, x):
        if root:
            check(root.left, x)
            x.append(root.data)
            l.append(root.data)
            check(root.right, x)
        l.sort()
        if l == x:
            return 'Yes'
        else:
            return 'No'

    print(check(root, x))



