# This algorithm eliminates branch prediction
# So we don't have any miss penalty here

def abs(x):
   y = x >> 31
   return (x + y) ^ y

a = -2 ** 32
print(abs(a))
b = 13
print(abs(b))
a = 0
print(abs(a))
b = 7
print(abs(b))
