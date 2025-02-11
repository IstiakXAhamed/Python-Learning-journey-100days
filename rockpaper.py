import random
Rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print("Welcome to our game ?!")
cpu = random.randint(1,3)
user=int(input("Input 1 for rock,2 for paper, 3 for scissor !!!"))

print("user :\n")
if user==1:
    print(Rock)
elif user==2:
    print(Paper)
elif user==3:
    print(Scissors) 
else:
    print('''
     _                         _
    |_|                       |_|
    | |         /^^^\         | |
   _| |_      (| "o" |)      _| |_
 _| | | | _    (_---_)    _ | | | |_ 
| | | | |' |    _| |_    | `| | | | |
\          /   /     \   \          /
 \        /  / /(. .)\ \  \        /
   \    /  / /  | . |  \ \  \    /
     \  \/ /    ||Y||    \ \/  /
       \_/      || ||      \_/
                () ()
                || ||
               ooO Ooo
''')           

print("CPU :\n")
if cpu==1:
    print(Rock)
elif cpu==2:
    print(Paper)
else:
    print(Scissors) 

if cpu==user:
    print("DRAW!")    
elif cpu==1 and user==2:
    print("User win")  
elif cpu==1 and user==3:
    print("CPU win") 
elif cpu==2 and user==1:
    print("CPU win")         
elif cpu==2 and user==3:
    print("User win")
elif cpu==3 and user==1:
    print("User win")    
elif cpu==3 and user==2:
    print("CPU win")    
else:
    print("Invalid!!!")   
    print('''
     _                         _
    |_|                       |_|
    | |         /^^^\         | |
   _| |_      (| "o" |)      _| |_
 _| | | | _    (_---_)    _ | | | |_ 
| | | | |' |    _| |_    | `| | | | |
\          /   /     \   \          /
 \        /  / /(. .)\ \  \        /
   \    /  / /  | . |  \ \  \    /
     \  \/ /    ||Y||    \ \/  /
       \_/      || ||      \_/
                () ()
                || ||
               ooO Ooo
''') 