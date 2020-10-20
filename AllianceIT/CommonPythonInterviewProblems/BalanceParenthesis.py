
def balanceParenthesis(s):
    # odd values will always be false in s
    if len(s)%2!=0:
        return False

    opening = set('([{')
    matches = set([('(',')'),('[',']'),('{','}')])

    stack = []

    for value in s:
        if value in opening:
            stack.append(value)

        else:
            if len(stack)==0:
                return False
            last_open = stack.pop()

            if (last_open, value) not in matches:
                return False

    return len(stack) == 0

def main():
    s = '()()[}'
    print(balanceParenthesis(s))

main()