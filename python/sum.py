import time

def Sum(l):
   return reduce(lambda x,y: x+y, l)

def loop_sum(l):
   __sum = 0
   for i in l:
      __sum += i

   return __sum

x = [i for i in range(10000001)]
start = time.time()
print(loop_sum(x))
end = time.time()
print("Using traditional loop: " + str(end-start) + "\n\n")

start = time.time()
print(Sum(x))
end = time.time()
print("Using lambda calculus: " + str(end-start) + "\n\n")

start = time.time()
print(sum(x))
end = time.time()
print("Using built-in function: " + str(end-start))
