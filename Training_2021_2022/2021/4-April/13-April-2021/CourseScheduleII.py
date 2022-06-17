'''
    There are a total of n courses you have to take labelled from 0 to n - 1.

    Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means 
    you must take the course bi before the course ai.

    Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering 
    of courses you should take to finish all courses.

    If there are many valid answers, return any of them. If it is impossible to finish all courses, 
    return an empty array.

    Example 1:

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. 
    So the correct course order is [0,1].

    Example 2:

    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both 
    courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

    Example 3:

    Input: numCourses = 1, prerequisites = []
    Output: [0]

'''
from collections import defaultdict, deque
def solve(numberOfCourses, courses):

    graph = defaultdict(list)
    queue = deque()

    inDegree = dict()
    
    # create the graph
    for targetCourse, preCourse in courses:
        graph[preCourse].append(targetCourse)
        # inDegree.get(targetCourse is just for retrieving the course and 0 is for initialization)
        inDegree[targetCourse] = inDegree.get(targetCourse, 0) + 1

    # find the initial course that doesn't have any prerequisite
    for course in range(numberOfCourses):
        if course not in inDegree:
            queue.append(course)
    
    # declare the topological sort to store the results
    topologicalSortOrder = []

    # do BFS to append the adjacent courses of each vertex
    while queue:
        currentCourse = queue.popleft()
        topologicalSortOrder.append(currentCourse)

        if currentCourse in graph:
            for adjacentCourse in graph[currentCourse]:
                # make sure to subtract 1 to each adjacent node
                inDegree[adjacentCourse] -=1

                if inDegree[adjacentCourse] == 0:
                    queue.append(adjacentCourse)

    return topologicalSortOrder if len(topologicalSortOrder) == numberOfCourses else []
    #print(topologicalSortOrder)

def main():

    numberOfCourses = 4
    courses = [[1,0],[2,0],[3,1],[3,2]]
    res = solve(numberOfCourses, courses)
    print(res)

main()