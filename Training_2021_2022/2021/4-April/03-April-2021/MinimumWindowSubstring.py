from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_cnt = Counter(t)
        start, end, found = 0, len(s)-1, 0
        min_win = ""
        for end in range(len(s)):
            # if you find the pattern then set the sum to +1
            if target_cnt[s[end]]>0:
                found += 1
            target_cnt[s[end]] -=1
            # Start shrinking the window
            while found==len(t):
                # determine if the current min window is less than current pointers distance
                if not min_win or end-start+1<len(min_win):
                    # get the new window
                    min_win = s[start:end+1]
                # increase the counter index, so you can get out later of the loop
                target_cnt[s[start]]+=1
                if target_cnt[s[start]]>0:
                    found -=1
                # move the starting pointer
                start+=1
        return min_win

def main():
    s = "ADOBECODEBANC"
    pattern = "ABC"
    solution = Solution()
    res = solution.minWindow(s, pattern)
    print(res)

main()