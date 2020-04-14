from arrayStack import Empty

def main():
    stack = ArrayStack()
    stack.push(5)
    stack.push(10)
    print(stack.is_empty())
    print("Success!")

class ArrayStack():
    '''LIFO stack implementation using Python. The last element inserted is the first one to go out.'''

    def __init__(self):
        '''Create an empty stack'''
        self._data = []             # non public list instance

    def __len__(self):
        '''Return the number of elements in the stack.'''
        return len(self._data)

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return len(self._data) == 0

    def push(self, e):
        '''Add element e to the top of the stack.'''
        self._data.append(e)

    def top(self):
        '''Return (but do not remove) the element at the top of the stack.'''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        '''Remove and return the element from the top of the stack.
           Raise an empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

if "__main__" == __name__:
    main()