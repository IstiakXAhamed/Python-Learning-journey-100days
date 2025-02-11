
import sys
import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def dealCard():
    return random.choice(cards)

def compare(userscore,computerscore):
    if computerscore==userscore:
        display()
        print(f"Computers final hand cards: {computer_cards},computer score: {computerScore}")
        print("The match is Draw!")
    elif computerscore==0:
        display()
        print(f"Computers final hand cards: {computer_cards},computer score: {computerScore}")
        print("You lose!. computer won blackJack!!")    
    elif userscore==0:
        display()
        print(f"Computers final hand cards: {computer_cards},computer score: {computerScore}")
        print("You got blackJack , You win!")
    elif userscore>21:
        display()
        print(f"Computers final hand cards: {computer_cards},computer score: {computerScore}")
        print("You Lose!")    
    elif computerscore>21:
        display()
        print(f"Computers final hand cards: {computer_cards},computer score: {computerScore}")
        print("You win!")    
    else:
        if userscore>computerscore:
            display()
            print(f"Computers final hand cards: {computer_cards},computer score: {computerScore}")
            print("You Win!!")   
        elif computerscore>userscore:
            display()
            print(f"Computers final hand cards: {computer_cards},computer score: {computerScore}")  
            print("You Lose!!")  
           
def calculateScore(cards):
    score = sum(cards)
    ace_count = cards.count(11)
    
    # Adjust for Aces if necessary
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
        
    # Check for a Blackjack
    if score == 21 and len(cards) == 2:
        return 0
    else:
        return score

def display():
    print(f"You cards: {user_cards}, Your score: {userScore}")
    print(f"Computers first card: {computer_cards[0]}")
    
def flush_input():
    if sys.stdin in ('\n', '\r\n'):
        sys.stdin.flush()    
    
moreGame=True
while moreGame:
    flush_input()
    os.system('cls')
    print(logo.logo)
    user_cards = []
    computer_cards = []
    user_cards.append(dealCard())
    user_cards.append(dealCard())
    computer_cards.append(dealCard())
    computer_cards.append(dealCard())
    
    computerGameEnds=False
    gameEnds=False
    userScore=calculateScore(user_cards)
    computerScore=calculateScore(computer_cards)
    display()
    if userScore==0 or userScore>21 or computerScore==0:
        print(f"Computers final hand cards: {computer_cards},computer score: {computerScore}")
        print("Game ends!!!")
        gameEnds=True
        
    while gameEnds!=True:
        moreDraw=input("You want to pick another card ,y or n?")
        if moreDraw=="y":
            user_cards.append(dealCard())
            userScore=calculateScore(user_cards)
            display()
            if userScore==0 or userScore>21 or computerScore==0:
                print(f"Computers final hand cards: {computer_cards},computer score: {computerScore}")
                print("Game ends!!!")
                gameEnds=True
                computerGameEnds=True
        elif moreDraw=='n':
            computerGameEnds=False
            break
    while computerScore<17:
        computer_cards.append(dealCard())
        computerScore=calculateScore(computer_cards)
    if computerScore > 21 and not computerGameEnds:
        print(f"Computers final hand cards: {computer_cards},computer score: {computerScore}")
        print("Computer busted! You win!")
        gameEnds=True
        
    if gameEnds==False:
        compare(userScore,computerScore)   
                      
    playAgain = input("You want to play again?y  or n?")
    if playAgain=='y':
        moreGame=True
    else:
        moreGame=False    