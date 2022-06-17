'''
    An image is represented by a 2-D array of integers, each integer representing the pixel value of the image 
    (from 0 to 65535).

    Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, 
    and a pixel value newColor, "flood fill" the image.

    To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally 
    to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally 
    to those pixels (also with the same color as the starting pixel), and so on. 
    Replace the color of all of the aforementioned pixels with the newColor.

    At the end, return the modified image. 

    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
'''

def solve(matrix, sr, sc, newColor):
    visited = set()
    targetColor = matrix[sr][sc]
    if matrix[sr][sc]== targetColor:
        dfs(matrix, sr, sc, newColor, targetColor, visited)
    
    # I don't need to visit all the nodes
    #for x in range(sr, len(matrix)):
    #    for y in range(sc, len(matrix[0])):
    #        if matrix[x][y]== targetColor:
    #            dfs(matrix, x, y, newColor, targetColor)
    return matrix

def dfs(matrix, xPos, yPos, newColor, targetColor, visited):
    visited.add((xPos, yPos))
    matrix[xPos][yPos] = newColor
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for direction in directions:
        newXPosition = direction[0]+xPos
        newYPosition = direction[1]+yPos
        if (validate(matrix, newXPosition, newYPosition) 
        and matrix[newXPosition][newYPosition]== targetColor 
        and (newXPosition, newYPosition) not in visited):
            dfs(matrix, newXPosition, newYPosition, newColor, targetColor, visited)

def validate(matrix, newXPosition, newYPosition):
    rows = len(matrix)
    cols = len(matrix[0])
    if newXPosition < 0 or newYPosition <0 or newXPosition>= rows or newYPosition>=cols:
        return False
    return True

def main():
    image1 = [[1,1,1],[1,1,0],[1,0,1]]
    image2 = [[1,2,1,1],[2,1,1,2],[1,0,1,0]]
    image3 = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 2
    newColor2 = 3
    newColor3 = 1
    res = solve(image2, sr, sc, newColor2)
    print(res)

main()
