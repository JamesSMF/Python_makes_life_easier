def sqSum(ls):
   return reduce(lambda x,y: x+y, map(lambda x: x**2, ls))

if __name__=="__main__":
   print(sqSum([1,2,3,4,5,6,7,8,9,10]))
