import time

def Prod():
   return reduce(lambda x,y: x*y, [1]+list(range(1, 100001)))

def loop_prod(l):
   __prod = 1
   for i in range(1,l+1):
      __prod *= i

   return __prod

x = 100000
start = time.time()
#  print(loop_prod(x))
loop_prod(x)
end = time.time()
print("Using traditional loop: " + str(end-start) + "\n\n")

start = time.time()
#  print(Prod())
Prod()
end = time.time()
print("Using lambda calculus: " + str(end-start) + "\n\n")
