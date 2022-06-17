
def solution(words):

    d = dict(list())
    # convert all the letters to lowercase

    for word in words:        
        vector = [0 for _ in range(26)]

        for letter in word:
            index = ord(letter.lower()) - ord('a')
            vector[index]+=1

        # a list as a key is NOT hashable, you need to convert this to a tuple, so you can find it in the dictionary
        # the keys in a dictionary must be immutable, that's why we need to use a tuple 
        vector_tuple = tuple(vector)
        if vector_tuple in d:
            d[tuple(vector)].append(word)
        else:
            d[tuple(vector)] = [word]
    
    return d.values()


def main():
    words = ["duel", "dule", "speed", "spede", "deul", "cars", "BED", "DEB"]
    res = solution(words)
    print(res)

main()

'''
    1. Generate the vector of 0 and 1
    2. for each letter of each word do a subtraction of words to find the key index, so you will use that key index in the vector
    3. repeat for all the words

    Time complexity: O(n*k)
    Space complexity: O(n*k)

'''