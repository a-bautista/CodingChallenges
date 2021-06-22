'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

[0,1],[1,2],[2,3]
in order to take course 1 you need to take course 0
in order to take course 2 you need to take course 1
in order to take course 3 you need to take course 2
This is possible, return True.

[0,1],[1,2],[2,3] [3,1]
This is not possible because it says that in order to take course
1 you need to take course 3 but this breaks the order because you
can take course 2 if you have already taken course 1. return False

Directed graph because we have a source and destination.
'''

from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        edges = [[] for _ in range(numCourses)]
        # [[],[0],[1],[2]]
        # degrees represent the visited nodes
        degrees = [0] * numCourses
        # [0,0,0,0]
        # below is going to indicate if the graph is connected
        # or if it is the last node which is not connected
        # [1, 1, 1, 0] which represent processed nodes (0) and not processed nodes (1)
        for course, pre_course in prerequisites:
            edges[pre_course].append(course)
            degrees[course] += 1

        queue = deque()
        # find the last course which is not connected (destination), in this case 3 is the course which is not connected
        for course, degree in enumerate(degrees):
            if not degree:
                queue.append(course)

        while queue:
            course = queue.popleft()
            for next_course in edges[course]:
                # I start with the last course (destination) and then I go down to the rest of the courses
                degrees[next_course] -= 1
                if not degrees[next_course]:
                    queue.append(next_course)

        return not sum(degrees)

def main():
    courses = [[0,1],[1,2],[2,3]]
    solution = Solution()
    res = solution.canFinish(4, courses)
    print(res)

main()

'''
    Algorithm: BFS Topological Sorting
    # Time: O(E + V)
    # Space: O(E + V)
'''