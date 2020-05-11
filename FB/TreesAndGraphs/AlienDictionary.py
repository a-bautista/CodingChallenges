from collections import deque


def find_order(words):
  if len(words) == 0:
    return ""

  # a. Initialize the graphs in degree and graph with parent-child letter.

  # graph = {
  #         'b':[], 'a':[], 'c':[]
  #       }

  # in_degree = {
  #           'b':0, 'a':0, 'c':0
  #     }

  inDegree = {}  # count of incoming edges
  graph = {}  # adjacency list graph
  for word in words:
    for character in word:
      inDegree[character] = 0
      graph[character] = []

  # b. Build the graph

  # Count the number of incoming edges for each letter and add the
  # add the parent - child letter.
  # graph = {'b':['a'], 'a':['c', 'c'], 'c':[]}
  # in_degree = { 'b': 0, 'a':1, 'c':2}

  for i in range(0, len(words)-1):
    # find ordering of characters from adjacent words
    w1, w2 = words[i], words[i + 1]
    for j in range(0, min(len(w1), len(w2))):
      parent, child = w1[j], w2[j]
      if parent != child:  # if the two characters are different
        # put the child into it's parent's list
        graph[parent].append(child)
        inDegree[child] += 1  # increment child's inDegree
        break  # only the first different character between the two words will help us find the order

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  sortedOrder = []
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # if sortedOrder doesn't contain all characters, there is a cyclic dependency between characters, therefore, we
  # will not be able to find the correct ordering of the characters
  if len(sortedOrder) != len(inDegree):
    return ""

  return ''.join(sortedOrder)


def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()


"""

  Input: Words: ["cab", "aaa", "aab"]
  Output: cab
  Explanation: From the given words we can conclude the following ordering among its characters:
   
  1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
  2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'
   
  From the above two points, we can conclude that the correct character order is: "cab"
  
  
  Algorithm:
  
    1. We need to start building a dictionary that will hold each letter and
    another dictionary that will hold the number of incoming edges for each letter.
    
    in_degree = {'b':0, 'a':0, 'c':0}
    graph     = {'b': [], 'a':[], 'c':[]}
    
    We are using the Kahn algorithm to create the dictionary for calculating the 
    incoming edges,  and then we use a Q to store the 'sources'. While there's an element
    in the Q, we popleft() an element and store it in a list which will hold the order of 
    elements. If there's a child in the extracted node then decrease its number of incoming 
    edges and if the incoming edge = 0 then add it to the Q. Repeat the process until no more 
    elements are in the Q.  

    Time complexity:
      O(V+E) where 'V' is the total number of different characters and 'E' is the total number of
      rules (Edges) in the alien language. Each pair of words can give us one rule, so the limit of 
      the rules depende on the size of the array of the words or O(N), thus, the time complexity of 
      the algorithm is O(V+N).  
    
    Space complexity:
      O(V+N) since we are storing all of the rules for each character in an adjacency list. 

"""