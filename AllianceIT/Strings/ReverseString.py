class Solution:
    def solve(self, s):
        s_list = list(s)
        left = 0
        right = len(s)-1
        while left <= right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left +=1
            right -=1
        return "".join(s_list)


def main():
    s = 'Hey Alejandro'
    solution = Solution()
    res = solution.solve(s)
    print(res)

main()