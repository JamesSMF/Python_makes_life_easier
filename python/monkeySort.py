import random

# This function checks if the list is sorted by increasing order
def is_sorted(theList):
   for i in range(1, len(theList)):       # traverse the entire list
      if theList[i] < theList[i-1]:  # if some item is smaller than the previous one
         return False           # it is not sorted
   return True      # if all items are in their own correct place, return true
# end def

s = raw_input("Please enter the numbers, splited by space: \n")    # get the input as string
data = map(int, s.split())       # convert the string into a list of numbers

while not is_sorted(data):       # while the list is not sorted
   random.shuffle(data)     # shuffle all the items in the list
# end while

print data      # print the sorted list
