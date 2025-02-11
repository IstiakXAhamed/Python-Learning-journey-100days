import random
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
playContinue = True

while playContinue:
    moreBlkjk=input("Do you want to have another game of Blackjack!, y or n?")
    if(moreBlkjk=="y"):
        myCard = []
        pcCard = []
        takeCard = True
        count = 2
        pcCount=2
        myCard.append(deal_card())
        myCard.append(deal_card())
        print(f"Your Cards: {myCard}")
        score = myCard[0]+myCard[1]
        print(f"current score: {score}")
        pcFcard = deal_card()
        pcCard.append(pcFcard)
        pcCard.append(deal_card())
        pcScore= pcCard[0]+pcCard[1]
        print(f"computer's first card: {pcFcard}")
        while pcScore<22:
            pcCard.append(deal_card())
            pcScore+=pcCard[pcCount]
            if 11 in pcCard and pcScore > 21:
                score -= 10  # Change the Ace value from 11 to 1
            pcCount+=1
        while takeCard:
            morePlay = input("y for getting more card,n for stop!")
            if(morePlay=="y"):
                if(score<21 and pcScore<21) :
                    myCard.append(deal_card())
                    score+= myCard[count]
                    print(f"Your Cards: {myCard}")
                    print(f"current score: {score}")
                    print(f"computer's first card: {pcFcard}")
                    count+=1
                    if 11 in myCard and score > 21:
                        score -= 10  # Change the Ace value from 11 to 1

                    if score > 21:
                        print("You went over. You lose!")
                        break
                    elif score == 21:
                        print("You hit 21! You win!")
                        break
                else:
                    if(score>21):
                        print(f"Your final hand: {myCard}, final score {score}")            
                        print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                        print("You went over. you lose!") 
                           
                    elif(pcScore>21):
                        print(f"Your final hand: {myCard}, final score {score}")            
                        print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                        print("Computer went over. Computer lose!") 
                       
                    elif(score==21):
                        print(f"Your final hand: {myCard}, final score {score}")            
                        print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                        print("You Win")
                        
                    elif(pcScore==21):
                        print(f"Your final hand: {myCard}, final score {score}")            
                        print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                        print("You Lose!")  
                    break        
            elif(morePlay=="n"):
                takeCard=False
                if(score>21):
                    print(f"Your final hand: {myCard}, final score {score}")            
                    print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                    print("You went over. you lose!")                   
                elif(pcScore>21):
                    print(f"Your final hand: {myCard}, final score {score}")            
                    print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                    print("Computer went over. Computer lose!")
                elif(score==21):
                        print(f"Your final hand: {myCard}, final score {score}")            
                        print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                        print("You Win")
                        
                elif(pcScore==21):
                        print(f"Your final hand: {myCard}, final score {score}")            
                        print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                        print("You Lose!")  
                             
                elif(score<21 and pcScore<21):
                    if(score>pcScore):
                        print(f"Your final hand: {myCard}, final score {score}")            
                        print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                        print("You Win")    
                    elif(score<pcScore):         
                        print(f"Your final hand: {myCard}, final score {score}")            
                        print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                        print("You Lose")
                    elif(score==pcScore):
                        print(f"Your final hand: {myCard}, final score {score}")            
                        print(f"Computer's final hand: {pcCard}, final score {pcScore}")    
                        print("The match is a Draw!")   
    elif(moreBlkjk=="n"):   
        playContinue=False                     