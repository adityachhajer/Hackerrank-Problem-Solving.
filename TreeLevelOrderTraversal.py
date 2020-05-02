class Queue(object):
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return self.items==[]
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
    def peek(self):
        if not self.is_empty():
            return self.items[-1].info


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def levelOrder(root):
    if root is None:
        return
    queue=Queue()
    queue.enqueue(root)
    traversal = ""
    while(len(queue))>0:
        traversal+=(str(queue.peek())+ " ")
        node=queue.dequeue()
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    print( traversal)




# Write your code here


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)