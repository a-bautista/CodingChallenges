#from collections import Counter
def solve(str1, k):
    '''
        1. I need to create a sort of Counter in a stack to keep the track of the letters.
        2. I need to establish some cases When the current letter from the input is NOT the same as the previous one:
            2.1. If the currentStack is greater than K then do a pop of the last list containing the letters.
            2.2. If the stack contains an element and the current letter from the string is similar to the 
                 last letter in the stack then add a +1
            2.3. if the current input letter is not the same as the last letter we have in our stack then add the 
                letter.
            2.3. Else just add the current input letter to the stack.
        3. Do a pop in case we have some additional letters in our stack > K.
        4. Print out the result
    '''
    
    stack = [[str1[0],1]]    
    for letterIndex in range(1, len(str1)):

        # if stack[-1][1]>=k:
        #     stack.pop()

        # same letters
        if str1[letterIndex] != str1[letterIndex-1]:

            # check if we can do a pop
            if stack[-1][1]>=k:
                stack.pop()
            
            # the current letter from the string is also located at the top of the stack
            if stack and str1[letterIndex]== stack[-1][0]:
                stack[-1][1]+=1
            
            # the current letter doesn't exist in our stack, then add it
            else:
                stack.append([str1[letterIndex], 1])
            
        # same letter, then keep adding the count of +1 to the current stack
        else:
            stack[-1][-1]+=1    

    if stack[-1][1]>=k:
        stack.pop()

    output = []
    for letter in stack:
        output+= letter[0]*letter[1]    
    return "".join(output)


def main():
    res = solve("dddabbbbaccccaax",3)
    print(res)
    #print(candy_crush("aabbbacd")) #cd
    #print(candy_crush("aabbccddeeedcba")) #blank expected
    #print(candy_crush("dddabbbbaccccaax")) #x

main()

'''
    Time complexity: O(nk)
    Space complexity: O(1) because of the stack
'''