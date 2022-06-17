def solve(nums, target):
        res = []

        def backtrack(residual, combination, nextNumber):
            if residual == 0:
                # you must use the list keyword, otherwise it will fail
                res.append(list(combination))
            elif residual < 0:
                return 
            else:
                for current in range(nextNumber, len(nums)):
                    combination.append(nums[current])
                    backtrack(residual - nums[current], combination, current)
                    #backtrack
                    combination.pop()

        backtrack(target, [], 0)
        return res

def main():
    candidates = [2,3,5] # prime numbers
    target = 13
    res = solve(candidates, target)
    print(res)

main()
