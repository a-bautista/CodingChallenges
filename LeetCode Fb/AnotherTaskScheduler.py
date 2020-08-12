'''

You're given a list of tasks, with number denoted different type of tasks,
and there'll be interval between tasks with tasks of same id.
Return total time for executing this task list.

solve([1, 1, 2, 1], 2)
return 7

'''

from collections import defaultdict


def solve(tasks, n):
    time = 0
    hash_table = dict()
    for i in range(len(tasks)):
        idle = 0

        if tasks[i] in hash_table:
            length = time - hash_table[tasks[i]]
            idle = max(n - length, 0)

        time += idle + 1
        hash_table[tasks[i]]=time
    return time


res = solve([1, 1, 2, 1], 2)
print(res)