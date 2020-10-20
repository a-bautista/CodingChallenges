'''
Each given array will have at least 1 number. There will be at least
two non-empty arrays.

The total number of the integers in all the m arrays will be in the
range of [2, 10000].

The integers in the m arrays will be in the range of [-10000, 10000].
'''

class MathSolution:
    def maxDistance(self, arrays):
        minnum = arrays[0][0]
        maxnum = arrays[0][-1]
        maxdiff = float('-inf')

        for array in arrays[1:]:
            maxdiff = max(maxdiff, array[-1] - minnum, maxnum - array[0])
            minnum = min(minnum, array[0])
            maxnum = max(maxnum, array[-1])
        return maxdiff

class Solution(object):
    def maxDistance(self, m):
        # naive approach
        res = float('-inf')
        m.sort()
        i=0
        while i < len(m)-1:
            current = m[i]
            next_to = m[i+1]
            for c in current:
                for n in next_to:
                    res = max(abs(c-n),res)
            i+=1

        # last round of comparison
        current = m[-1]
        next_to = m[0]
        for c in current:
            for n in next_to:
                res=max(abs(c-n),res)
        return res

def main():
    m = [[1,2,3],[4,5],[1,2,3]]
    m2 = [[-10,-9,-9,-3,-1,-1,0],[-5],[4],[-8],[-9,-6,-5,-4,-2,2,3],[-3,-3,-2,-1,0]]
    solution = Solution()
    sol = MathSolution()

    res = solution.maxDistance(m2)
    res2 = sol.maxDistance(m2)
    print(res)
    print(res2)

main()