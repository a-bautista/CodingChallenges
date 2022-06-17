'''
    You have to implement the trace_path() function which will take in a list of source-destination pairs 
    and return the correct sequence of the whole journey from the first city to the last.
    [["Boston", "Texas"] , ["Texas", "Missouri"] , ["Missouri", "NewYork"] , ["NewYork", "Chicago"]]
'''

def trace_path(my_dict):
    result = []
    # Create a reverse dict of the given dict i.e if the given dict has (N,C)
    # then reverse dict will have (C,N) as key-value pair
    # Traverse original dict and see if it's key exists in reverse dict
    # If it doesn't exist then we found our starting point.
    # After the starting point is found, simply trace the complete path
    # from the original dict.
    reverse_dict = dict()
    # To fill reverse dict, iterate through the given dict
    # Get the keys from the key and then reverse them
    keys = my_dict.keys()
    for key in keys:
        # here you are reversing the dictionary by getting the value based on the key
        reverse_dict[my_dict.get(key)] = key
    # Find the starting point of itinerary
    from_loc = None
    
    # Get the keys from the reversed dictionary
    #keys_rev = reverse_dict.keys()

    # here you need to find the starting point which shouldn't be in the reverse dictionary
    for key in keys:
        if key not in reverse_dict:
            from_loc = key
            break
            # Trace complete path
    # you find where are you heading next based on the initial starting point
    to = my_dict.get(from_loc)
    # start traveling 
    while to is not None:
        result.append([from_loc, to])
        from_loc = to
        # get the next value based on the key 'to'
        to = my_dict.get(to)
    return result

def main():
    my_dict = dict()
    my_dict["NewYork"] = "Chicago"
    my_dict["Boston"] = "Texas"
    my_dict["Missouri"] = "NewYork"
    my_dict["Texas"] = "Missouri"
    print(trace_path(my_dict))

main()