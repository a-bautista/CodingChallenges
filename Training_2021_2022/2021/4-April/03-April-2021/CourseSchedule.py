from collections import deque
def solveGraphBFS(courses, numOfCourses):
    queue = deque()
    # create the graph based on the numOfCourses
    graph = [[] for _ in range(numOfCourses)]
    # create the visited nodes
    visited = [0]*numOfCourses

    # create the graph instead of using a defaultdict and set the visited array to 1
    for courseIndex, preCourse in courses:
        graph[preCourse].append(courseIndex)
        visited[courseIndex]+=1

    # find the course that is not connected 
    for index, visitedNode in enumerate(visited):
        if not visitedNode:
            queue.append(index)
    
    # BFS graph
    while queue:
        currentNode = queue.popleft()
        for nextCourse in graph[currentNode]:
            visited[nextCourse]-=1
            if not visited[nextCourse]:
                queue.append(nextCourse)

    return not sum(visited)

def main():
    courses = [[0,1],[1,2],[2,3]]
    res = solveGraphBFS( courses, 4)
    print(res)

main()
    

