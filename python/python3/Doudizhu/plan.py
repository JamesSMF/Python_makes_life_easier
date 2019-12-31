# 所有可能性：
# 单张，对子，三张，顺子，炸弹，连对，三带一，三带二，飞机，飞机带俩，四带二

# first move
for 所有的我方手牌的key：
   if 对应value是1 （打单张）：
      for 对方手牌的value为1的key：
         list_of_card = 找出比这张我方手牌大的牌
         for 所有的list_of_card里的牌：
            找出我方比这张牌大的牌中的最小牌
            if 要不起：
               heuristic value不变，手牌不变，进入被动状态
            else:
               计算这条path的综合值=heuristic value + （原来的总手牌数-剩下的手牌数）

   if 对应的value
