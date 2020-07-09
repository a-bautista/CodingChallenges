
'''
Intro
------------------------
func 0:
start
0

func 1
start 
2

func 1
end
4

func 0
end
7


         func 1  func 1
        |------||---|
  func 0                func 0          
|-------|            |----------| 

+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7


This is an invalid case, because two functions won't start or end at the same time. 

         func 1            func 1
        |------|           |---|
  func 0           func 0          
|-------|       |----------| 

+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7

Algorithm explanation
----------------------------------------------------------------------------

Func 0 is running in the background once func 1 starts, so I can add these functions in a stack.
Once the function ends then I need to count the previous time for that function and add it to the current time. 
I need to remove the function from the stack once it ends. 
The I need to consider the previous time from the function that was running in the background. 



initial variables
----------------------------------------------------------------------------
input:
func_id
type: 'start or end'
time
k which is the total number of functions

ans = [] # result
stack_functions = []
previous_time = 0

'''

def exclusive_time_penalty(logs, k):
    ans = [0] * k
    #stack = SuperStack()
    stack = []

    for log in logs:
        fn, typ, time = log.split(':')
        fn, time = int(fn), int(time)

        if typ == 'start':
            stack.append(time)
        else:
            delta = time - stack.pop() + 1
            ans[fn] += delta
            #stack.add_across(delta)
            stack = [t+delta for t in stack] #inefficient


def exclusiveTime(logs, k):
    ans = [0] * k
    functions = []
    prev_time = 0

    for log in logs:
        func_id, type, time = log.split(':')
        func_id, time = int(func_id), int(time)

        if type == 'start':

            # if there are previous functions already running
            if functions:
                # get the last function
                last_func = functions[-1]

                # add the count of the current time - previous time (because we want to count the current
                # blocks of time which is the running total (time) - the previous blocks (prev_time)
                ans[last_func] += time - prev_time

            # add the functions to the stack and add the current time into the previous time
            functions.append(func_id)
            prev_time = time

        else:
            # Get the last index of the stack and do a pop
            remove_idx = functions.pop()

            # add the the previous time that we had in the array to the function that ended
            # and subract the previous time because this time was already stored in the array
            # add 1 to solve the problem of indexes not counted
            ans[remove_idx] += time - prev_time + 1
            prev_time = time + 1
    return ans





def main():
    number_of_functions = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    res = exclusiveTime(logs,number_of_functions)
    print(res)

main()

'''
    Time complexity: O(N) because of the number of functions
    Space complexity: O(N) because of the stack

'''