# 1. Implementera en STACK (klass) enl specifikation i Dag 3 - Mer strukturer

class Stack:

    # Exempel of stack with LIFO and more.
    def __init__(self,capacity:int = 10):
        self.max_capacity = capacity

        self._data = []
        self.max_capacity = capacity

    def push(self,value: any):
        if self.is_full ():
            raise ValueError("Stack is full")
        else:
            self._data.append(value)
        
    def is_full(self) -> bool:
        return len(self._data) >= self.max_capacity
    
    def is_empty(self):
        return len(self._data) == 0
        
        
    def pop(self):
        return self._data.pop()
        

if   __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(2)
    my_stack.push(4)
    my_stack.push(0)
    my_stack.push(6)
    my_stack.push(7)
    my_stack.push(21)

    last_item = my_stack.pop()
    last_item = my_stack.pop()
    last_item = my_stack.pop()
    last_item = my_stack.pop()
    last_item = my_stack.pop()
    last_item = my_stack.pop()
    if not my_stack.is_empty():
        last_item = my_stack.pop()
    else:
        print ("Stack is empty")