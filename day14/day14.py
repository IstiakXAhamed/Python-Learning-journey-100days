import game_data
import art
import random
def compare(a,b):
    if(game_data.data[a]['follower_count']>game_data.data[b]['follower_count']):
        return 'A'
    else:
        return 'B'
    
score=0

gameON=True
while gameON:
    print(art.logo)
    compA = random.randint(0,49)
    compB = random.randint(0,49)
    print(f"Compar A: {game_data.data[compA]['name']}, a {game_data.data[compA]['description']}, from {game_data.data[compA]['country']}")
    print(art.vs)
    print(f"Against B: {game_data.data[compB]['name']}, a {game_data.data[compB]['description']}, from {game_data.data[compB]['country']}")
    userChoice=input("who has more followers ? Type 'A' or 'B': ").upper()
    key= compare(compA,compB)
    if(userChoice==key):
        score+=1
        gameON=True
    else:
        if(key=='A'):
            result = compA
            
        else:
            result = compB            
        print(f"You Lose ! {game_data.data[result]['name']} has got {game_data.data[result]['follower_count']}!!")
        print(f"Your final score : {score}")
        gameON=False

            
        
        
    