'''
    Given the list of lists [1,[1,2,3,4],[4,5,6]], flatten the list, so you get a result like:

    [1,1,2,3,4,5,6].
'''

def solve(list1):

    res = []

    def rec(list1):
        for element in list1:
            if isinstance(element, list):
                rec(element)
            else:
                res.append(element)
    rec(list1)
    return res

def main():
    list1 = [1,[1,2,3,4],[4,5,6]]
    sol = solve(list1)
    print(sol)

main()

    