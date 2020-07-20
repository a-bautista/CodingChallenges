'''
    You are given a m*n grid. You are asked to generate k mines on this grid randomly. Each cell should
    have equal probability of k / m*n of being chosen

'''

import random

# m,n : Size of grid
# k : Number of mines
def plant(m,n,k):
    s = m*n
    cs = s
    selected = []
    grid = [0] * s
    for i in range(k):
        p = random.randint(0,cs-1)
        pc = 0
        for p2 in range(s):
            if grid[p2]==0:
                # Empty cell
                if pc==p:
                    # Found the p-th empty cell
                    break
                pc += 1
        selected.append(p2)
        grid[p2] = 1 # Block the cell
        cs -= 1
    selected = [(s%m,s//m) for s in selected]
    return selected


def main():
    k_mines = 3
    width = 3
    height = 3
    res = plant(width, height, k_mines)
    print(res)

main()

'''
    Time complexity: O(Mkn)
'''