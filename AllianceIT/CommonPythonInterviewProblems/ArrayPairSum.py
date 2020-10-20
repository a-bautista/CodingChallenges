'''
    Given an integer array, output all the unique pairs that sum up to
    a specific value k.

    [1,3,3,2,5], 5
    output: (3,2)

    [1,3,3,2,5]
     ^       ^

     1+5 = 6 and 6 > 5 lower right

     count = 1+3 == 5 False
     count = 1+3 == 5 False
     count = 1+2 == 5 False
     count = 1+5 == 5 False
'''

def solve(arr, target):

    # edge case
    if len(arr)==0:
        return

    # num2 = target - num1

    # because they are asking us for unique pairs, we use sets
    seen = set()
    output = set()

    for num in arr:

        # num1 + num = target
        num1 = target - num

        # if you haven't seen num1 that adds up to target, then add the number
        # that adds up to num1
        if num1 not in seen:
            seen.add(num)

        # you have the numbers that add up the pair
        else:
            output.add((min(num1, num),max(num1, num)))

    return '\n'.join(map(str, list(output)))


def main():
    arr = [1,3,2,2]
    target = 4
    print(solve(arr, target))

main()

