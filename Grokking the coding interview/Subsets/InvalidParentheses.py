class Solution:
    def removeInvalidParentheses(self, s):
        # initialize a set with one element
        # set is used here in order to avoid duplicate element
        level = {s}

        # in the first pass, you verify if the input is valid and if not then generate
        # all possible combinations of the string
        while True:
            valid = []
            # append all the correct combinations
            for elem in level:
                if self.isValid(elem):
                    valid.append(elem)
            if valid:
                return valid
            # initialize an empty set
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
        return count == 0

def main():

    solution = Solution()
    res = solution.removeInvalidParentheses('()())()')
    print(res)

main()