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
         print i

theStack = Stack()
theStack.push(42)
theStack.push(32)
theStack.push(98)
theStack.pop()
theStack.pop()
theStack.push(101)
theStack.printStack()
