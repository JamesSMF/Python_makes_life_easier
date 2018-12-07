from __future__ import print_function

class Stack(object):
   theList = [1]
   del theList[0]
   elem = 0

   def push(self, num):
      self.theList.append(num)
      self.elem = self.elem + 1

   def pop(self):
      self.elem = self.elem - 1
      temp = self.theList[self.elem]
      del self.theList[self.elem]
      return temp

   def isEmpty(self):
      if self.elem == 0:
         return True
      else:
         return False

   def printStack(self):
      for i in self.theList:
         print(i, end = '')


theString = "How's your day going?"
theStack = Stack()
for char in  theString:
   theStack.push(char)

while not theStack.isEmpty():
   print(bytes(theStack.pop()), end='');
print('', end = '\n');
