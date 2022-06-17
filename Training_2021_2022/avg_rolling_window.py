def solve(nums, k):
    a = 0
    avg_vals = []
    length = len(nums)
    for i in range(0, length - k + 1):
        c_val = 0
        for j in range(i, k + a):
            c_val += nums[j]
        avg_vals.append([c_val/k])
        a += 1
    return avg_vals
'''
    Good but how can you improve it? 
'''

def main():
    nums = [1, 2, 3, 4, 5]
    k = 3
    res = solve(nums, k)
    print(res)

main()
