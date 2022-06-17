class Solution:
    def removeDuplicatesI(self, s):
        stack = []
        for c in s:
            if len(stack)>0:
                if c != stack[-1]:
                    stack.append(c)
                # adjacent duplicates
                else:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


def main():
    s = 'aabbzq'
    solution = Solution()
    res = solution.removeDuplicatesI(s)
    print(res)

main()

'''
   Time complexity: O(N)
   Space complexity: O(N)    
'''