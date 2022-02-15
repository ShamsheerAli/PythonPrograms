
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def set_cards():
  player1=[]
  player2=[]
  for i in range (2):
     player1.append(random.choice(cards))
     player2.append(random.choice(cards))
  print(player1)
  print(player2)
  if(10 in player1 and 11 in player1):
      print("Player 1 won")
  if(10 in player2 and 11 in player2):
      print("player 2 won")  
  sum1=sum(player1)
  sum2=sum(player2)  
  if(sum1>21):
      if(11 in player1):
          for x in range (player1(len)):
               if(player1(x)==11):
                   player1[x]=1
                   sum1=sum(player1)
  print(sum1)                   
set_cards()
