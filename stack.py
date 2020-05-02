class Stack:
    def __init__(self):
        self.items=[]

    def len(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def get_stack(self):
        return self.items

s=Stack()
s.push("A")
s.push("B")
s.pop()

print(s.get_stack())

