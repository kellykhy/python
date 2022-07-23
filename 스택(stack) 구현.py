# stack in pyton

'''
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.stack.pop()
        return pop_object

    def top(self):
        top_object = None
        if self.isEmpty():
            print("Stack ifs Empty")
        else:
            top_object = self.stack[-1]
        return top_object
    
    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.pop()
print(stack1.stack)
'''

class Stack():
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, data):
        self.stack.append(data)
        self.top += 1
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.stack.pop()
            self.top -= 1
        return pop_object

    def top_obj(self):
        top_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.stack[self.top]
        return top_object

    def isEmpty(self):
        is_empty = False
        if self.top == -1:
            is_empty = True
        return is_empty

def move(stack_a, stack_b):
    if not stack_a.isEmpty() and not stack_b.isEmpty() and stack_a.top_obj() < stack_b.top_obj():
        stack_b.push(stack_a.pop())
        return 1
    else:
        return 0

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1.stack)

stack2 = Stack()
stack2.push(5)
stack2.push(4)
print(stack2.stack)


move(stack1, stack2)
print(stack1.stack)
print(stack2.stack)