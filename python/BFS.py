graph ={
   "A" : ["B", "C"],
   "B" : ["A", "C", "D"],
   "C" : ["A", "B", "D", "E"],
   "D" : ["B", "C", "E", "F"],
   "E" : ["C", "D"],
   "F" : ["D"]
}

# This method does broad-first search of a graph
# The first input entry is the graph (as a dict() form)
# The second input entry is the starting node
def BFS(graph, node):
   queue = []             # using a queue to implement the traversal
   queue.append(node)     # put the starting node into the queue
   seen = set()           # all the nodes that have been traversed
   seen.add(node)         # add starting node to seen
   result = []            # a list to store the result
   while len(queue) > 0:  # while the queue is not empty
      vertex = queue.pop(0)           # pop the frontmost node out
      connectedNodes = graph[vertex]  # store all its connected nodes
      for w in connectedNodes:  # for any node which is connected to it
         if w not in seen:      # if that node has not yet appeared
            queue.append(w)     # append that new node to the queue
            seen.add(w)         # and that node has appeared now
      result.append(vertex)     # store the vertex node into result
   return result                # return the result list

print BFS(graph, "B")           # print out the result list
