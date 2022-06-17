'''
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
    take course bi first if you want to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

    Return true if you can finish all courses. Otherwise, return false.

    Example 1:

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.

    Example 2:

    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also 
    have finished course 1. So it is impossible.

    Algorithm:

    You need to create a data structure for [[0,1],[1,2],[2,3]]:
        0:[1]
        1:[2]
        2:[3]
    And have a count to indicate which course doesn't depend from another. For this, you can have a count:
    
    visited = [0]* numberOfCourses
    visited[courseIndex]+=1

    Then do a BFS, to traverse all the nodes and decrease the visited[courseIndex] by 1. If at the end the sum is
    0 then return not 0 which will be true.

'''

from collections import defaultdict, deque
def solveGraphBFS(courses, numberOfCourses):

    graph = defaultdict(list)
    visited = [0] * numberOfCourses
    queue = deque()

    for targetCourse, preCourse in courses:
        graph[preCourse].append(targetCourse)
        # below is the "set" that we will use to determine which course is not connected
        visited[targetCourse]+=1

    # find the course that is not connected, that is, the not visited course should have a value of 0
    for index, visitedCourse in enumerate(visited):
        # that is, if there's a 0 value to the index of that course then add it to the queue
        if not visitedCourse: 
            queue.append(index)

    while queue:
        currentCourse = queue.popleft()
        for nextCourse in graph[currentCourse]:
            visited[nextCourse]-=1
            if not visited[nextCourse]:
                queue.append(nextCourse)
    
    return not sum(visited)

def main():
    courses = [[0,1],[1,2],[2,3]]
    courses2 = [[1,0]]
    res = solveGraphBFS( courses, 4)
    print(res)

main()

