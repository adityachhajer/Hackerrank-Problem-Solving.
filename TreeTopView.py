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


def topView(root):
    if root is not None:
        dict={}
        node_dict={}
        que=[]
        que.append(root)
        node_dict[root.info]=0
        while len(que) > 0 :
            temp=0
            cur=que.pop(0)
            if cur is not None:
                level=node_dict[cur.info]
                if level in dict:
                    pass
                else:
                    temp=cur.info
                    dict[level]=temp


                if cur.left:
                    left_node=cur.left
                    que.append(left_node)
                    node_dict[left_node.info]=node_dict[cur.info] - 1

                if cur.right:
                    right_node=cur.right
                    que.append(right_node)
                    node_dict[right_node.info]=node_dict[cur.info] + 1
        l=[]
        for i in sorted(dict):
            l.append(dict[i])
        print(*l)
        # print(dict)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)