import re

class Solution(object):
   def moveZeroes(self, nums):
	   """
      :type nums: List[int]
      :rtype: void Do not return anything, modify nums in-place instead.
      """
      nums[:] = ([value for value in nums if value != 0] + nums.count(0) * [0])
