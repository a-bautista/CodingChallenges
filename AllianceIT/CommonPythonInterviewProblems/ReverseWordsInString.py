from collections import deque
def reverseWordsInString(s):

    # simple approach
    # " ".join(reversed(s.split(" ")))

    ######## interview approach ###########

    left, right = 0, len(s) - 1
    # remove leading spaces
    while left <= right and s[left] == ' ':
        left += 1

    # remove trailing spaces
    while left <= right and s[right] == ' ':
        right -= 1

    d, word = deque(), []

    # push word by word in front of deque
    while left <= right:

        if s[left] == ' ' and word:
            d.appendleft(''.join(word))
            word = []
        # join letter by letter
        elif s[left] != ' ':
            word.append(s[left])
        left += 1
    d.appendleft(''.join(word))
    return ' '.join(d)


def simpleSol(sentence):

    words = []
    i = 0

    while i<=len(sentence)-1:

        if sentence[i]!=' ':
            word_start = i

            while i <= len(sentence)-1 and sentence[i]!= ' ':
                i += 1

            words.append(sentence[word_start:i])
        i+=1

    res = []
    for i in range(len(words)-1,-1,-1):
        res.append(words[i])
    print(" ".join(res))


def main():
    print(reverseWordsInString("The   dog is happy  "))
    simpleSol("  The dog is happy   i")

main()

'''
    Time complexity: O(N)
    Space complexity: O(N)
'''