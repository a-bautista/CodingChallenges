def candy_crush(input):
    # edge case
    if not input:
        return input
    
    stack = []
    # start adding the first letter
    # this stack indicates the letter and the total count of that letter
    stack.append([input[0], 1])
    
    for i in range(1, len(input)):
        # if the next letter is different from the last letter from the current input
        if input[i] != input[i-1]:
            # clear the stack only if the top letters in the stack have more than 3 letters
            if stack[-1][1] >= 3:
                stack.pop()
            # add the incoming letter in case it is the same as the one we have at the top of the stack
            # this applies after a pop has been made
            if stack and stack[-1][0] == input[i]:
                stack[-1][1] += 1
            # add the incoming letter in case it is different as the one we have at the top of the stack
            else:
                stack.append([input[i], 1])
        # keep adding letters to the stack
        else:
            stack[-1][1] += 1
            
    # handle end in case you have more than 3 same letters at the end of the iteration
    if stack[-1][1] >= 3:
        stack.pop()

    # start printing the letters in the result
    out = []
    for ltrs in stack:
    # append the result to the list
        out += ltrs[0] * ltrs[1]
    
    return ''.join(out)
    
#print(candy_crush("aaaabbbc")) #c
print(candy_crush("aabbbacd")) #cd
print(candy_crush("aabbbccda")) #cd
#print(candy_crush("aabbccddeeedcba")) #blank expected
print(candy_crush("dddabbbbaccccaax")) #x

'''
    Time complexity: O(nk)
    Space complexity: O(1) because of the stack
'''