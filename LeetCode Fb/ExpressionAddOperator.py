'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Basically, you need to create the DFS because you will create something like the following:
1
1+2
1+2+3 (valid)

1+2
1+2-3

1+2
1+2*3

1
1-2
1-2+3

1-2
1-2-3

1
1*2
1*2+3

1*2
1*2+3

1*2
1*2-3

1*2
1*2*3 (valid)

1+23
1-23
1*23

12+3
12-3
12*3

123

'''

class Solution:
    def addOperators(self, num, target):

        def backtracking(idx=0, path='', value=0, prev=None):
            # once you find a value which is equal to the target then append the result
            # into the list
            if idx == len(num) and value == target:
                rtn.append(path)
                return

            # start and end are used for taking the values in the num variable
            start = idx + 1
            end = len(num) +1
            for i in range(start, end):

                # take the next value in the num variable and then use it for the prev value
                tmp = int(num[idx: i])

                if i == idx + 1 or (i > idx + 1 and num[idx] != '0'):
                    # enter only when you have the first value to start or when
                    # you will append more values, i.e., 1, 12, 123
                    if prev is None:
                        backtracking(i, num[idx: i], tmp, tmp)

                    else:
                        # for each
                        backtracking(i, path + '+' + num[idx: i], value + tmp, tmp)
                        backtracking(i, path + '-' + num[idx: i], value - tmp, -tmp)
                        backtracking(i, path + '*' + num[idx: i], value - prev + prev * tmp, prev * tmp)
        rtn = []
        backtracking()
        return rtn

def main():
    num = "123"
    target = 6
    solution = Solution()
    res = solution.addOperators(num, target)
    print(res)

main()

'''
    Time complexity: O(N*4**N) because we have 4 different recursive paths. Then N represents 
    the length of the expression. 
    Space complexity: O(N)
'''