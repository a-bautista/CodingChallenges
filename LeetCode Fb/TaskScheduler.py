"""
    Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters
    represent different tasks. Tasks could be done without original order. Each task could be done in one interval.
    For each interval, CPU could finish one task or just be idle.

    However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals
    that CPU are doing different tasks or just be idle.

    You need to return the least number of intervals the CPU will take to finish all the given tasks.

    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8

    Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

    The number of tasks is in the range [1, 10000].
    The integer n is in the range [0, 100].

"""
from collections import Counter

def leastInterval(tasks, n):

    tasks_count = list(Counter(tasks).values())

    max_count = max(tasks_count)

    idle_time = max_count - 1

    max_count_tasks = tasks_count.count(max_count) # count the number of times the max_count appears in the list

    return max(len(tasks), idle_time * (n + 1) + max_count_tasks)

def main():
    #tasks = ["A", "B", "C","A","B","C"]
    tasks = ["A", "A", "A", "B", "B", "C", "C"]
    #tasks = ["A", "A", "A", "A", "A", "A", "B","C"]
    #tasks = ["A","A","A","A","A","A","B","C","D","E"]
    #tasks = ["A","A","A","A","B","B","B","B","C","C","C","C","D","D","D"]

    n = 2
    res = leastInterval(tasks,n)
    print(res)

main()
