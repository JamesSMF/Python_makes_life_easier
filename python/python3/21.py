# -*- coding: utf-8 -*-

from random import randint

def main():
   print("欢迎来玩21点，规则你应该懂，我就不说了。")
   while(win_or_lose()):
      print("\n现在你有" + str(user_point) + "点")
      print("电脑有" + str(comp_point) + "点")
      uBet = prompt_bet()
      cBet = comp_bet()
      print("电脑赌了" + str(cBet) + "点")
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
      judge(compSum, userSummation(), uBet, cBet)

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

def prompt_bet():
   print("赌多少？")
   bet = input()
   while(int(bet) > user_point):
      print("\n你没有你想象的那么富有。\n赌多少")
      bet = input()

   while(int(bet) < 0):
      print("\n有点道德，至少赌个1块钱吧。")
      bet = input()

   if(int(bet) == user_point):
      print("\n一把梭哈还行！牛逼！")

   return int(bet)

def comp_bet():
   if(comp_point > 600):
      bet = 1000 - comp_point
   elif(comp_point > 300):
      bet = int(comp_point / 4)
   elif(comp_point > 200):
      bet = int(comp_point / 3)
   elif(comp_point > 30):
      bet = int(comp_point / 2)
   else:
      bet = comp_point

   return bet

def prompt():
   print("直接摊牌还是继续抽牌？（A. 摊牌 B. 继续发牌）")
   user_choice = "C"
   while(user_choice!="A" and user_choice!="B" and user_choice!="a" and user_choice!="b"):
      print("请选择A或B")
      user_choice = input()
   return user_choice

def win_or_lose():
   if(user_point >= 1000 or comp_point <=0):
      print("你赢了！你的最终得分是：" + str(user_point))
      return 0
   elif(user_point <= 0 or comp_point >= 1000):
      print("你输了！请离开赌场，欢迎下次光临。")
      return 0
   else:
      return 1

def judge(compS, userS, uBet, cBet):
   print("电脑的牌为： " + str([display[item] for item in comp_hand]))
   print("\n你的点数为：" + str(userS))
   print("电脑点数为：" + str(compS))
   if(compS<=21 and userS>21):
      lose(uBet, cBet)
   elif(compS>21 and userS<=21):
      win(uBet, cBet)
   elif(compS<=21 and userS<=21):
      if(compS==userS):
         if(len(user_hand) >= 5 and len(comp_hand) < 5):
            win(uBet, cBet)
         elif(len(user_hand) < 5 and len(comp_hand) >= 5):
            lose(uBet, cBet)
         elif(len(user_hand) < len(comp_hand)):
            win(uBet, cBet)
         elif(len(user_hand) > len(comp_hand)):
            lose(uBet, cBet)
         else:
            draw()
      else:
         if(compS > userS):
            lose(uBet, cBet)
         elif(compS < userS):
            win(uBet, cBet)
         else:
            draw()
   else:
      draw()

def init_condition():
   if(len(user_hand) > 0):
      user_hand.clear()
   if(len(comp_hand) > 0):
      comp_hand.clear()
   for i in range(2):
      init_card = randint(1,13)
      user_hand.append(init_card)
      cards[init_card] += 1
      init_card = randint(1,13)
      comp_hand.append(init_card)
      cards[init_card] += 1

   # tell the player what they have now
   print("\n现在你手上有：" + str([display[items] for items in user_hand]) + "\n")

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

def win(uBet, cBet):
   print("恭喜，你赢了！")
   global user_point
   user_point += uBet
   global comp_point
   comp_point -= cBet

def lose(uBet, cBet):
   print("抱歉，你输了！")
   global comp_point
   comp_point += cBet
   global user_point
   user_point -= uBet

def draw():
   print("平局。打得不错！")

# initial conditions
# global variables
cards = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
display = {1:"A", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", 11:"J", 12:"Q", 13:"K"}
user_hand = list()
comp_hand = list()
user_point = 500
comp_point = 500

main()

