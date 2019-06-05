# 射人先射马，擒贼先擒王
# 数船就数船头
# 别扯DFS，loop套loop，不虚就是莽

def countBattleships(board):
   """
   :type board: List[List[str]]
   :rtype: int
   """

   # count the number of battleships

   count = 0

   if len(board)==0 or len(board[0])==0:
      return 0

   for i in range(0,len(board)):
      for k in range(0, len(board[0])):
         if board[i][k]=='X':
            if(k<len(board[0])-1 and board[i][k+1]!='X') and (i<len(board)-1 and board[i+1][k]!='X'):
               count += 1
            elif(i==len(board)-1 and k<len(board[0])-1 and board[i][k+1]!='X') or (k==len(board[0])-1 and i<len(board)-1 and board[i+1][k]!='X'):
               count += 1
            elif i==len(board)-1 and k==len(board[0])-1:
               count += 1
   return count

inputList = [['X','.','.','X'],['X','.','.','X'],['.','.','.','X']]
print(countBattleships(inputList))
