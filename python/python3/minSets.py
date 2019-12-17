def minSets(ls):
   """
   ls is a list of sets
   return a list of minSets in ls
   """

   ans = list()
   for c in ls:
      if not any(c1<c for c1 in ls) and not any(c1<=c for c1 in ans):
         ans.append(c)

   return ans

if __name__ == '__main__':
   ls = [{2, 3, 4}, {2, 3}, {6, 2, 3}, {2, 3}, {2, 4, 5}]
   print(minSets(ls))
