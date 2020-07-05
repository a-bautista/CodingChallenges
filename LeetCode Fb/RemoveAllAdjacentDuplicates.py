class Solution:
    def removeDuplicates(self, s):
        res = []

        for char in s:
            if res and res[-1]==char:
                res.pop()
            else:
                res.append(char)

        return "".join(res)

def main():
    s = 'aabbzq'
    solution = Solution()
    res = solution.removeDuplicates(s)
    print(res)

main()

'''
   Time complexity: O(N)
   Space complexity: O(N)    
'''