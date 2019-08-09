# TODO
# J,Q,K 全部搞成10
# 增加积分系统
# 两张牌比小老虎大



from random import randint

def main():
   init_condition()
   selection = prompt()
   while(selection=="B" or selection=="b"):
      newCard = deal(1)
      print("\n你被发到了一张" + newCard)
      print("现在你拥有的手牌：" + str([display[el] for el in user_hand]))
      if(userSummation()>21):
         break
      selection = prompt()

   compSum = comp_turn()
   judge(compSum, userSummation())

def comp_turn():
   compSum = compSummation()

   while(compSum < 17):
      deal(2)
      compSum = compSummation()                    # update the sum

   return compSum

def compSummation():
   compSum = sum(comp_hand)
   for i in range(len(comp_hand)):
      if(comp_hand[i]==11 or comp_hand[i]==12 or comp_hand[i]==13):
         compSum -= (comp_hand[i]-10)

   for i in range(len(comp_hand)):
      if(comp_hand[i]==1):
         if(compSum+10 <= 21):
            compSum += 10

   return compSum

def userSummation():
   userSum = sum(user_hand)
   for i in range(len(user_hand)):
      if(user_hand[i]==11 or user_hand[i]==12 or user_hand[i]==13):
         userSum -= (user_hand[i]-10)

   for i in range(len(user_hand)):
      if(user_hand[i]==1):
         if(userSum+10 <= 21):
            userSum += 10

   return userSum

def prompt():
   print("直接摊牌还是继续抽牌？（A. 摊牌 B. 继续发牌）")
   user_choice = "C"
   while(user_choice!="A" and user_choice!="B" and user_choice!="a" and user_choice!="b"):
      print("请选择A或B")
      user_choice = input()
   return user_choice

def judge(compS, userS):
   print("电脑的牌为： " + str([display[item] for item in comp_hand]))
   print("\n你的点数为：" + str(userS))
   print("电脑点数为：" + str(compS))
   if(compS<=21 and userS>21):
      lose()
   elif(compS>21 and userS<=21):
      win()
   elif(compS<=21 and userS<=21):
      if(compS==userS):
         if(len(user_hand) >= 5 and len(comp_hand) < 5):
            win()
         elif(len(user_hand) < 5 and len(comp_hand) >= 5):
            lose()
         elif(len(user_hand) < len(comp_hand)):
            win()
         elif(len(user_hand) > len(comp_hand)):
            lose()
         else:
            draw()
      else:
         if(compS > userS):
            lose()
         elif(compS < userS):
            win()
         else:
            draw()
   else:
      draw()

def init_condition():
   for i in range(2):
      init_card = randint(1,13)
      user_hand.append(init_card)
      cards[init_card] += 1
      init_card = randint(1,13)
      comp_hand.append(init_card)
      cards[init_card] += 1

   # tell the player what they have now
   print("现在你手上有：" + str([display[items] for items in user_hand]) + "\n")

def deal(num):
   additional_card = randint(1,13)
   while(cards[additional_card]>=4):         # make sure there are no five cards with the same number
      print(cards[additional_card])
      additional_card = randint(1,13)
   if(num==1):
      user_hand.append(additional_card)
   else:
      comp_hand.append(additional_card)

   return display[additional_card]           # return a string

def win():
   print("恭喜，你赢了！")

def lose():
   print("抱歉，你输了！")

def draw():
   print("平局。打得不错！")

# initial conditions
# global variables
cards = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
display = {1:"A", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", 11:"J", 12:"Q", 13:"K"}
user_hand = list()
comp_hand = list()
init_point = 500

main()



