# brackets

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def empty(self):
        return not self.items
    
    def top(self):
        return self.items[-1]
    
C = input()
opening = '({['
closing = ')}]'

for i in range(int(C)):
    case = input()
    stack = Stack()
    cnt_o = 0
    wrong= True
    for c in case:
        if c in opening:
            stack.push(c)
            cnt_o += 1
        else:
            if stack.empty():
                wrong = False
                break
            if (opening.find(stack.top()) != closing.find(c)):
                break
            stack.pop()
            
    if stack.empty() and cnt_o != 0 and wrong:
        print("YES")
    else:
        print("NO")