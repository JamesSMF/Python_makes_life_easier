import fileinput

out = open("DataBase.txt", "w")
wordCount = dict()

for line in fileinput.input():
   line = line.replace('A', 'a');
   line = line.replace('B', 'b');
   line = line.replace('C', 'c');
   line = line.replace('D', 'd');
   line = line.replace('E', 'e');
   line = line.replace('F', 'f');
   line = line.replace('G', 'g');
   line = line.replace('H', 'h');
   line = line.replace('I', 'i');
   line = line.replace('J', 'j');
   line = line.replace('K', 'k');
   line = line.replace('L', 'l');
   line = line.replace('M', 'm');
   line = line.replace('N', 'n');
   line = line.replace('O', 'o');
   line = line.replace('P', 'p');
   line = line.replace('Q', 'q');
   line = line.replace('R', 'r');
   line = line.replace('S', 's');
   line = line.replace('T', 't');
   line = line.replace('U', 'u');
   line = line.replace('V', 'v');
   line = line.replace('W', 'w');
   line = line.replace('X', 'x');
   line = line.replace('Y', 'y');
   line = line.replace('Z', 'z');

   line = line.replace('?', ' ');
   line = line.replace('.', ' ');
   line = line.replace(',', ' ');
   line = line.replace('!', ' ');
   line = line.replace(':', ' ');
   line = line.replace(';', ' ');
   line = line.replace('[', ' ');
   line = line.replace(']', ' ');

   stringList = line.split()
   for word in stringList:
      if word not in wordCount:    # if the word is not in the dict
         wordCount[word] = 1
      else:                        # if the word has already existed
         wordCount[word] = wordCount[word] + 1  # increment freq by 1

      # end if-else
   # end for

# To this point, dict is created. Now we should print out the result. #



# finaldic = sorted(wordCount, key = len)
i = 1
for word in wordCount:
   if len(word) == i:
      finaldic = dict()
      finaldic = sorted(wordCount, key = wordCount.get)
      for items in finaldic:
         out.write(items + " " + bytes(finaldic.get(items)))   # print
      # end for
      i = i + 1
   # end if
# end for

fileinput.close()





