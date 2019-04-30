class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        # initialize a default dict with all 0's
        theWall = collections.defaultdict(lambda : 0)
        for line in wall:    # look at each line
            i = 0
            for brick in line[:-1]:    # take sum from right to left
                i += brick
                theWall[i] += 1

        # plus a [0] to prevent empty sequence
        return len(wall)-max(theWall.values()+[0])
