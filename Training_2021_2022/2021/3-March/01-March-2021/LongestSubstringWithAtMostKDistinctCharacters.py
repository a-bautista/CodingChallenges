
def solve(str1, k):
    window_start =0
    char_frequency = dict()
    max_len = 0

    # 1. Start building the char frequency dictionary to know if you can continue increasing the max_len
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # this can be built with a defaultdict that accepts None values
        if right_char not in char_frequency:
            char_frequency[right_char] =0
        char_frequency[right_char]+=1
        # 2. If your char_frequency exceeded the k value, then shrink the char_frequency window
        while len(char_frequency)>k:
            left_char = str1[window_start]
            char_frequency[left_char] -=1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            # Increase the starting window, so you can move onto the next letters from the char_frequency
            window_start +=1
        max_len = max(max_len, window_end - window_start + 1)
    return max_len

def main():
    str1 = "araaci" # araa and k =2 then output = 4
    res = solve(str1,1)
    print(res)

main()

'''
    Time complexity: O(N)
    Space complexity: O(K)
'''