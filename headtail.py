

"""toss=input("")
selection = ("tails")
selection2 =("heads")
def rdd():
    def rdd1():
        def rdd2():
            if( selection == toss):
                print("you win : the coin  landed on" +" " + toss)
            elif(selection2 == toss):
                print("you loss : the coin  landed on" +" " + toss)

        def rdd3():      
            if(selection2 == toss) :
                print("you win : the coin  landed on" +" " + toss)
            elif(selection == toss):
                print("you loss : the coin  landed on" +" " + toss)
        
        return rdd2()
        return rdd3()

    
   
if __name__ == "__main__":rdd()"""

import random


coin=["heads","tails"]
toss=random.choice(coin)
selection=input("heads or tails:")


if selection == toss:
  print("you win : the coin  landed on" + toss)
else :
  print("you loss : coin  landed on +" + toss)
