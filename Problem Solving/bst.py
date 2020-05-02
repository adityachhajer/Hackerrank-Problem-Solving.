class Stack(object):
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            self.items.pop()
    def is_empty(self):
        return len(self.items)==[]
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return (len(self.items))

class Queue(object):
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items)==0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTres(object):
    def __init__(self,root):
        self.root=Node(root)

    def print_tree(self,traversal_type):
        if(traversal_type=='preorder'):
            return self.preorder_print(tree.root,"")
        elif(traversal_type=='Inorder'):
            return self.Inorder_print(tree.root,"")
        elif(traversal_type=='Postorder'):
            return self.Postorder_print(tree.root,"")
        elif(traversal_type=='level-order'):
            return self.levelorder_print(tree.root)
        elif(traversal_type=='reverse-level-order'):
            return self.reverse_levelorder_print(tree.root)
        else:
            print(traversal_type,"is not valid..!")


    def preorder_print(self,start,traversal):
        # Root->left->right
        if start:
            traversal+= (str(start.value)+" ")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    def Inorder_print(self,start,traversal):
        # left->root->right
        if start:
            traversal = self.Inorder_print(start.left,traversal)
            traversal+= (str(start.value)+" ")
            traversal = self.Inorder_print(start.right,traversal)
        return traversal

    def Postorder_print(self,start,traversal):
        # left->right->root
        if start:
            traversal = self.Postorder_print(start.left,traversal)
            traversal = self.Postorder_print(start.right,traversal)
            traversal+= (str(start.value)+" ")
        return traversal

    def levelorder_print(self,start):
        if start is None:
            return
        queue=Queue()
        queue.enqueue(start)
        traversal=""
        while(len(queue))>0:
            traversal+=(str(queue.peek())+" ")
            node=queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self,start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal=''
        while(len(queue))>0:
            node=queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack)>0:
            node=stack.pop()
            traversal+= str(node.value)+" "
        return traversal

    def height(self,node):
        if node is None:
            return -1
        left_height=self.height(node.left)
        right_height=self.height(node.right)

        return 1+ max(left_height,right_height)

tree=BinaryTres(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("Inorder"))
print(tree.print_tree("Postorder"))
print(tree.print_tree("level-order"))
# print(tree.print_tree("reverse-level-order"))

# print(tree.height(tree.root))