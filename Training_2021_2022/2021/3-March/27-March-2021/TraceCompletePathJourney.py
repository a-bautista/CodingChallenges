'''
    You have to implement the trace_path() function which will take in a list of source-destination pairs 
    and return the correct sequence of the whole journey from the first city to the last.
    [["Boston", "Texas"] , ["Texas", "Missouri"] , ["Missouri", "NewYork"] , ["NewYork", "Chicago"]]
'''

def solve(itinerary):
    keys = itinerary.keys()
    values = itinerary.values()
    fromCity = (keys - values).pop()
    sol = []
    #sol.append(fromCity)
    to = itinerary.get(fromCity)
    while to is not None:
        #sol.append(to)
        to = itinerary.get(fromCity)
        if fromCity is not None:
            sol.append(fromCity)
        fromCity = itinerary.get(to)
        if to is not None:
            sol.append(to)
        

    return sol



def main():
    itinerary = dict()
    itinerary['Boston'] = 'Texas'
    itinerary['Texas'] = 'Missouri'
    itinerary['Missouri'] = 'NewYork'
    itinerary['NewYork'] = 'Chicago'
    res = solve(itinerary)
    print(res)

main()