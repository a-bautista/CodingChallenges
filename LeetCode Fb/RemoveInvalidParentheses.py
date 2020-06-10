class Solution:
    def removeInvalidParentheses(self, s):
        # initialize a list with one element
        level = [s]
        print(type(level))
        # in the first pass, you verify if the input is valid and if not then generate
        # all possible combinations of the string
        while True:
            valid = []
            # append all the correct combinations
            for elem in level:
                # if the element is valid, then return True and append that combination into the
                # valid list, else if the element is not valid then that combination won't be added
                if self.isValid(elem):
                    valid.append(elem)
            if valid:
                return valid

            # initialize an empty set (the set can put the new elements in unsorted order
            new_level = set()
            # BFS: Generate all possible combinations
            for elem in level:
                for i in range(len(elem)):
                    new_level.add(elem[:i] + elem[i + 1:])
            level = new_level


    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0 # This means to return True

def main():

    solution = Solution()
    res = solution.removeInvalidParentheses('()())()')
    print(res)

main()

"""
    Time complexity: O(N * 2^N)
    Space complexity: O(n)
"""