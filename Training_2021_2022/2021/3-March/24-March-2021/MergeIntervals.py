def solve(intervals):

    # sort the array by the first element
    intervals.sort(key=lambda x:x[0])

    merged = []
    for interval in intervals:

        # not overlapping
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        
        # overlapping
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

def main():
    #solution = Solution()
    #res = solution.merge([[1,5], [3,7], [4,6], [6,8], [10,12], [11,15]])
    res =  solve([[1,5], [3,7], [4,6], [6,8], [10,12], [11,15]])
    print(res)

main()