from __future__ import print_function

class Stack(object):
   theList = []
   elem = 0         # has 0 element at first

   def push(self, num):             # push one item into the stack
      self.theList.append(num)
      self.elem = self.elem + 1

   def pop(self):                  # pop the top item out
      self.elem = self.elem - 1
      temp = self.theList[self.elem]
      del self.theList[self.elem]
      return temp

   def isEmpty(self):             # check if the stack is empty
      if self.elem == 0:
         return True
      else:
         return False

   def printStack(self):         # print the stack from bottom to top
      for i in self.theList:
         print(i, end = '')


theString = "How's your day going?"
theStack = Stack()
for char in  theString:
   theStack.push(char)

while not theStack.isEmpty():
   print(bytes(theStack.pop()), end='');
print('', end = '\n');
