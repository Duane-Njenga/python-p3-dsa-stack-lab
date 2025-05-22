class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            return self.full()
        self.items.append(item)
        

    def pop(self):
        if self.items:
            return self.items.pop()
        return None
         
        

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True 
        return False
    
    def search(self, target):
        for i, item in enumerate(reversed(self.items)):
            if item == target:
                return i 
        return -1  


# if __name__ == "__main__":
#     stk = Stack([1], 1)

#     print(stk.full())
#     # assert(stk.size() == 1)
#     # assert(stk.pop() == 1)
#     stk.push(1)
#     # stk.push(2)
#     print(stk.items)
#     print(stk.full())
#     # assert(stk.size() == 1)
#     # assert(stk.pop() == 1)