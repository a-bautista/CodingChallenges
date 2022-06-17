from collections import OrderedDict
def findFirstUnique(lst):
    # the ordered dict guarantees that elements are inserted as they appear in the array
    counts = OrderedDict()
    # create a dictionary based on a list
    counts = counts.fromkeys(lst, 0)
    for i in lst:
        counts[i]+=1
    
    for i in lst:
        if counts[i]==1:
            return i
    return -1
    

def main():
  lst = [4,5,1,2,0,4]
  res = findFirstUnique(lst)
  print(res)

main()