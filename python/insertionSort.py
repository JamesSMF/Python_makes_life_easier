def insSort(listOfInt):
   for itemIndex in range(1,len(listOfInt)):
      temp = listOfInt[itemIndex]
      inner = itemIndex
      while inner > 0 and listOfInt[inner-1] >= temp:
         listOfInt[inner] = listOfInt[inner-1]
         inner -= 1
      # end of while
      listOfInt[inner] = temp
      print listOfInt

theList = [31, 41, 59, 26, 41, 58]
insSort(theList)
