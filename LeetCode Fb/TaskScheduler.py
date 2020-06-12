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

    Further explanation: 
        
        The trick is in this line: there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals
        that CPU are doing different tasks or just be idle and this means:
        
        AAABBB, n=2
        
        A -> B -> idle -> A -> B -> idle -> A -> B
             1     2           1     2
             
        Every second time, you need to put it in idle because we have a repeated value.
        
        ABCABC, n=2 (best case)
        
        A -> B -> C -> A -> B -> C
             1    2    1    2
             
        We don't need to put the CPU in idle because we have different tasks.
        
        AAA, n=2 (worst case)
        
        A -> idle -> idle -> A -> idle -> idle -> A
               1       2            1       2
        
        AAAB, n=2
        
        A -> B -> idle -> A -> idle -> idle -> A
             1      2            1       2
        
    
        This problem follows the greedy approach because we need to look for the most repeated task.
    
        We need to calculate the idle time: 
            
            idle_time = ( max_occurring_task - 1 )
            
        We need to calculate the interval time:
        
            intervals = idle time * ( n + 1 )
            
        We need to calculate the number of times the max count appeared.
        
            max_count_tasks = number_max_occurring_tasks
            
        As a side note, the interval might not always be true because of this test case: 
        
            ABCABCDEFG, n=2
            
        A B C A B C D E F G, this doesn't follow the interval approach, so we need to use the max(len(tasks), intervals)
        
        
        
    
"""
from collections import Counter

def leastInterval(tasks, n):

    # convert the Counter of values to a list
    tasks_count = list(Counter(tasks).values())

    # get the max value that appear in the counter(converted to a list)
    max_count = max(list(tasks_count))

    # determine the idle time that will occur in the CPU
    idle_time = max_count - 1

    # count the number of times the max_count appears in the list
    max_count_tasks = tasks_count.count(max_count)

    interval = idle_time * (n + 1)

    return max(len(tasks), interval + max_count_tasks)

    #return max(len(tasks), idle_time * (n + 1) + max_count_tasks)

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
