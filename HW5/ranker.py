import fileinput
from collections import OrderedDict

out = open("FinalDataBase.txt", "a+")

for loop in range(1, 2):
   wordCount = dict()   # maps from word to frequency

   for line in fileinput.input():
      dataPair = line.split()
      if len(dataPair[0]) == 19 and int(dataPair[1]) == loop:
         word = dataPair[0]
         wordCount[word] = dataPair[1]

   # end for

   finaldic = OrderedDict(sorted(wordCount.items(), key=lambda x: x[0], reverse = True))
   for word in finaldic:
      out.write(word + " " + bytes(wordCount[word]) + "\n")

fileinput.close()

