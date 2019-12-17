import collections

def leastBricks(wall):
   """
   :type wall: List[List[int]]
   :rtype: int
   """

   # initialize a default dict with all 0's
   theWall = collections.defaultdict(lambda : 0)
   for line in wall:   # look at each line
      i = 0
      for brick in line[:-1]:   # take sum from right to left
         i += brick
         theWall[i] += 1

   # plus a [0] to prevent empty sequence
   return len(wall)-max(theWall.values()+[0])

wall = [[2,4,6,1],[1,1,7,2,2],[5,3,5],[4,2,6,1]]
sol = leastBricks(wall)
print(sol)
