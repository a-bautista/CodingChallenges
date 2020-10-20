class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def getDecimalValue(self, head):
        num = self.extract(head)
        res = self.convertBinarytoInt(num)
        return res

    def extract(self, node):
        res = []
        while node is not None:
            res.append(node.val)
            node = node.next
        return res

    def convertBinarytoInt(self, num):
        num.reverse()
        dec_num = 0
        for i in range(len(num)-1,-1,-1):
            if num[i]!=0:
                dec_num += 2**i
        return dec_num


def main():
    a = Node(1)
    b = Node(0)
    c = Node(1)
    a.next = b
    b.next = c
    c.next = None

    res = Solution()
    res.getDecimalValue(a)
    print(res)

main()