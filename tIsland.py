print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island!\n Your mission is to find the treasure!")

if input("left or right?")=="left":
    if input("swim or wait?")=="wait":
        if input("Which door?yellow , red or blue")=="yellow":
            print("Win")
        elif input()=="red":
            print("game over!")  
        elif input()=="blue":
            print("game over!")  
        else:
            print("invalid door !! looser!!")                
    else:
        print("game over!")    
else:
    print("game over !! ")
    print(''' ________ ___  ___  ________  ___  __    ___  __    ___  __             ___    ___ ________  ___  ___     
|\  _____\\  \|\  \|\   ____\|\  \|\  \ |\  \|\  \ |\  \|\  \          |\  \  /  /|\   __  \|\  \|\  \    
\ \  \__/\ \  \\\  \ \  \___|\ \  \/  /|\ \  \/  /|\ \  \/  /|_        \ \  \/  / | \  \|\  \ \  \\\  \   
 \ \   __\\ \  \\\  \ \  \    \ \   ___  \ \   ___  \ \   ___  \        \ \    / / \ \  \\\  \ \  \\\  \  
  \ \  \_| \ \  \\\  \ \  \____\ \  \\ \  \ \  \\ \  \ \  \\ \  \        \/  /  /   \ \  \\\  \ \  \\\  \ 
   \ \__\   \ \_______\ \_______\ \__\\ \__\ \__\\ \__\ \__\\ \__\     __/  / /      \ \_______\ \_______\
    \|__|    \|_______|\|_______|\|__| \|__|\|__| \|__|\|__| \|__|    |\___/ /        \|_______|\|_______|
                                                                      \|___|/                             ''')