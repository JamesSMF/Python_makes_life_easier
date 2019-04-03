# Description:
# Move all zeros in a list to the end of the list.
# e.g. original list: [1 0 2 4 6 0 9 7]
# Modified list: [1 2 4 6 9 7 0 0]

import re

class Solution(object):
   def moveZeroes(self, nums):
	   """
      :type nums: List[int]
      :rtype: void Do not return anything, modify nums in-place instead.
      """
      nums[:] = ([value for value in nums if value != 0] + nums.count(0) * [0])
