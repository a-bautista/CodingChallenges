from collections import deque
def solve(matrix):
    #steps = 0
    initialValue = matrix[0][0]
    queue = deque()
    queue.append(((0,0), 0))
    matrix[0][0] = 1 # the tree was cut off
    countZeroes = 1 # necessary for the rows with zeroes
    while queue:
        (currentX, currentY), steps = queue.popleft()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for direction in directions:
            newPosX = direction[0] + currentX
            newPosY = direction[1] + currentY

            if validate(matrix, newPosX, newPosY):
                # 
                if matrix[newPosX][newPosY] >= initialValue and matrix[newPosX][newPosY]!=1:
                    steps+=1
                    initialValue = matrix[newPosX][newPosY]
                    matrix[newPosX][newPosY] = 1
                    queue.append(((newPosX, newPosY),steps))
                    countZeroes-=1
                # cannot walk through
                elif matrix[newPosX][newPosY]==0:
                    countZeroes+=1
                

    if steps > countZeroes:
        return steps
    else:
        return -1

def validate(matrix, xPos, yPos):
    rows = len(matrix)
    cols = len(matrix[0])
    if xPos < 0 or yPos < 0 or xPos >= rows or yPos >= cols:
        return False
    return True

def main():
    forest  = [[1,2,3],[0,0,4],[7,6,5]]
    forest2 = [[1,2,3],[0,0,0],[7,6,5]]
    forest3 = [[2,3,4],[0,0,5],[8,7,6]]
    forest4 = [[1,2,0],[0,3,0],[0,4,5]]
    forest5 = [[54581641,64080174,24346381,69107959],
               [86374198,61363882,68783324,79706116],
               [668150,92178815,89819108,94701471],
               [83920491,22724204,46281641,47531096],
               [89078499,18904913,25462145,60813308]]

    res = solve(forest5)
    print(res)

main()

# [[54581641,64080174,24346381,69107959],
#  [86374198,61363882,68783324,79706116],
#  [668150,92178815,89819108,94701471],
#  [83920491,22724204,46281641,47531096],
#  [89078499,18904913,25462145,60813308]]