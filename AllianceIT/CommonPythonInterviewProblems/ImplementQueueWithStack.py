class Solution:

    def __init__(self):
        self.instack  = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):

        # If there are no elements in the outstack
        # len(self.outstack) == 0
        if len(self.outstack)==0:

            # edge case: when there are no elements in both stacks, return -1
            if len(self.instack)!=0:
                while len(self.instack)!=0:
                    self.outstack.append(self.instack.pop())
            else:
                return -1

        # if you have elements in both stacks, then you need
        # to switch elements
        if self.outstack and self.instack:

            while len(self.outstack)!=0:
                self.instack.append(self.outstack.pop())

            while len(self.instack)!=0:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


    def peek(self):
        return self.outstack[0]

    def size(self):
        return len(self.instack)

def main():
    solution = Solution()
    solution.enqueue(1)
    solution.enqueue(2)
    solution.enqueue(3)
    res = solution.size()
    print(res)

    popped = solution.dequeue()
    print(popped)
    popped2 = solution.dequeue()
    print(popped2)
    solution.enqueue(4)
    popped3 = solution.dequeue()
    print(popped3)
    solution.dequeue()
    res2 = solution.dequeue()
    print(res2)


main()
