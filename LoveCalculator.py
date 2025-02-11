print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
countForTrueN1 = name1.upper().count("T")+name1.upper().count("R")+name1.upper().count("U")+name1.upper().count("E")
countForTrueN2 = name2.upper().count("T")+name2.upper().count("R")+name2.upper().count("U")+name2.upper().count("E")
countForLoveN1 = name1.upper().count("L")+name1.upper().count("O")+name1.upper().count("V")+name1.upper().count("E")
countForLoveN2 = name2.upper().count("L")+name2.upper().count("O")+name2.upper().count("V")+name2.upper().count("E")
countTrue = str(countForTrueN1+countForTrueN2)
countLove = str(countForLoveN1+countForLoveN2)
loveScore = int(countTrue+countLove)
if loveScore<10 or loveScore>90: 
   print(f"Your score is {loveScore}, you go together like coke and mentos.")
   
elif loveScore>=40 and loveScore<=50:
   print(f"Your score is {loveScore}, you are alright together.")    
else:
   print(f"Your score is {loveScore}.")   