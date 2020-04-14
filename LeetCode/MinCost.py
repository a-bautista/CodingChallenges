import heapq

def min_cost_to_connect_all_ropes(ropes):
    if len(ropes) < 2:
        return 0

    ''' convert the list into a min heap (values go from the lowest to the highest in a binary tree). 
        See the image to understand how this algorithm works. 
        
        [8, 4, 6, 12] to [4, 8, 6, 12]
               4
            8     6
         12    
    '''


    heapq.heapify(ropes)
    print(ropes)
    res = 0
    #print(heapq.heappop(ropes)+heapq.heappop(ropes))


    while len(ropes) > 1:
        # remove the main node (the lowest value) and sum it with the next node (the next lowest value)
        sum = heapq.heappop(ropes) + heapq.heappop(ropes)
        #print(sum)
        res += sum
        heapq.heappush(ropes, sum)

    return res


ropes = [8, 4, 6, 12]
expected = 58
assert min_cost_to_connect_all_ropes(ropes) == 58

'''
ropes = [20, 4, 8, 2]
#expected = 54
assert min_cost_to_connect_all_ropes(ropes) == 54

ropes = [1, 2, 5, 10, 35, 89]
#expected = 58
assert min_cost_to_connect_all_ropes(ropes) == 224

ropes = [2, 2, 3, 3]
#expected = 58
assert min_cost_to_connect_all_ropes(ropes) == 20

'''
'''
    Given n ropes of different lengths, we need to connect these ropes into one rope. We can connect only 2 ropes at a time. 
    The cost required to connect 2 ropes is equal to sum of their lengths. The length of this connected rope is also equal to 
    the sum of their lengths. This process is repeated until n ropes are connected into a single rope. Find the min possible 
    cost required to connect all ropes.
    
    Input: ropes = [8, 4, 6, 12]
    Output: 58
    Explanation: The optimal way to connect ropes is as follows

    1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
    2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
    3. Connect the ropes of length 18 and 12 (cost is 30).
    Total cost to connect the ropes is 10 + 18 + 30 = 58
'''
