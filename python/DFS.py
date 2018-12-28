graph ={
   "A" : ["B", "C"],
   "B" : ["A", "C", "D"],
   "C" : ["A", "B", "D", "E"],
   "D" : ["B", "C", "E", "F"],
   "E" : ["C", "D"],
   "F" : ["D"]
}

# This method does depth-first search of a graph
# The first input entry is the graph (as a dict() form)
# The second input entry is the starting node
def DFS(graph, node):
   stack = []             # using a stack to implement the traversal
   stack.append(node)     # put the starting node into the stack
   seen = set()           # all the nodes that have been traversed
   seen.add(node)         # add starting node to seen
   result = []            # a stack to store the result
   while len(stack) > 0:  # while the stack is not empty
      vertex = stack.pop(-1)          # pop the last node out
      connectedNodes = graph[vertex]  # store all its connected nodes
      for w in connectedNodes:  # for any node which is connected to it
         if w not in seen:      # if that node has not yet appeared
            stack.append(w)     # append that new node to the stack
            seen.add(w)         # and that node has appeared now
      result.append(vertex)     # store the vertex node into result
   return result                # return the result list

print DFS(graph, "E")           # print out the result list
