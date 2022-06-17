'''
    input: ['ate', 'tan','nat','eat']
    output: [['ate','eat'],['tan','nat']]

    create a dictionary and its keys should have 0s or 1s depending on which letter was detected.

    {(1,0,0,0,1,0,0,0,...,1): [ate,eat]}

    provides you the letter value in numeric, i.e., letter e is 101
    ord(c)-ord('a')--> 101-97 = 4 then add +1 in the keys of the initial array [0 for _ range(27)]

    def solve(str1):
        #arr1 = []
        results = dict([])
        for word in str1:
            #temp = []
            arr1 = [0 for _ in range(27)]
            for letter in word:
                arr1[ord(c)-ord('a')]+=1
            
            if tuple(arr1) not in results:
                results[tuple(arr1)] = ''
            results[tuple(arr1)].append(word)
    return results.values()
                
'''

def solve(str1):
    results = dict([])
    for word in str1:
        arr1 = [0 for _ in range(27)]
        for letter in word:
            arr1[ord(letter)-ord('a')]+=1
        
        if tuple(arr1) not in results:
            # initialize the dictionary with empty lists
            results[tuple(arr1)] = []
        results[tuple(arr1)].append(word)
    return results.values()

def main():
    words = ['ate', 'tan','nat','eat']
    res = solve(words)
    print(res)

main()