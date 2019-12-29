############################################
# 斗地主解残局程序
# 半人工智能。为了保证运算速度，仅使用三层
# game tree。
#
# Heuristic Function采用了所有手牌点数的
# 平均数。
# 算法采用了A* Search。基于所剩手牌数和
# Heuristic Value综合评估得出的下一步move。
############################################

# init setup
userHand = dict()
compHand = dict()
#  display = {1:"A", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", 11:"J", 12:"Q", 13:"K"}
display = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}

# A > B ? True : False
def card_compare(A, B):
   return display[A] > display[B]

def heuristic(lst):
   curr_sum = reduce(lambda x,y: x+y, lst)
   return curr_sum / len(lst)

uStr = input("请输入用户手牌（不用输入花色），用空格分隔: ")
cStr = input("请输入电脑手牌（不用输入花色），用空格分隔: ")

# convert input into lists
uL = uStr.split(" ")
cL = cStr.split(" ")
hu = heuristic(uL)
hc = heuristic(cL)

# convert lists into dict() with counts
for i in uL:
   userHand[i] = userHand.get(i, 0) + 1

for i in cL:
   compHand[i] = compHand.get(i, 0) + 1

# unit test
print(userHand)
print(compHand)
# PASS

for card in userHand:



