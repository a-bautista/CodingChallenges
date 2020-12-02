class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for num in asteroids:
            if num>0:
                stack.append(num)
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(num):
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(num)
                elif stack[-1] == -num:
                    stack.pop()
        return stack

def main():
    nums = [-2,-1,1,2]
    solution = Solution()
    res = solution.asteroidCollision(nums)
    print(res)

main()