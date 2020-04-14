

def find_treasure(t_map, row, col, curr_steps, min_steps):



    if row >= len(t_map) or row < 0 or col >= len(t_map[0]) or col < 0 or t_map[row][col] == 'D' or t_map[row][col] == '#':
        return None, min_steps

    # when you find the treasure
    if t_map[row][col] == 'X':
        curr_steps += 1
        if min_steps > curr_steps:
            min_steps = min(curr_steps, min_steps)

        return None, min_steps

    else:
        tmp = t_map[row][col]
        t_map[row][col] = '#'
        curr_steps += 1
        left = find_treasure(t_map, row, col-1, curr_steps, min_steps)
        right = find_treasure(t_map, row, col+1, curr_steps, min_steps)
        up = find_treasure(t_map, row-1, col, curr_steps, min_steps)
        down = find_treasure(t_map, row+1, col, curr_steps, min_steps)

        t_map[row][col] = tmp

        return curr_steps, min(left[1], right[1], up[1], down[1])


if __name__ == '__main__':
    treasure_map = [['O', 'O', 'O', 'O'],['D', 'O', 'D', 'O'],['O', 'O', 'O', 'O'],['X', 'D', 'D', 'O']]

    res = find_treasure(treasure_map, 0, 0, -1, float('inf'))
    print("Result: ", res[1])


'''
   You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. 
   Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest 
   route to the treasure island. Assume the map area is a two dimensional grid, represented by a matrix of characters. 
   You must start from the top-left corner of the map and can move one block up, down, left or right at a time. 
   The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. 
   Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. 
   You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. 
   Output the minimum number of steps to get to the treasure.
   
   'O', 'O', 'O', 'O'
   'D', 'O', 'D', 'O'
   'O', 'O', 'O', 'O'
   'X', 'D', 'D', 'O'
   
'''