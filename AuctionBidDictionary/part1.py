import os
import art
def add_bid(name,bid):
        newBid= {
            "name":name,
            "bid" :bid  
            } 
        
        bidList.append(newBid)
#os.system('cls')
print(art.logo)

bidList =[]
listFinished = False
while listFinished!=True:
    os.system('cls')
    if input("is there are other users who want to bid?\n")=="yes":
        name=input("what is your name?\n")
        bid=int(input("how many $ you want to bid ?\n"))
        add_bid(name,bid)
        
    else:
        listFinished=True                
    
highest_bid = 0
highest_name = ""
for item in bidList:
    if highest_bid<item["bid"]:
        highest_bid=item["bid"]
        highest_name=item["name"]
print(f"Highest bid is done by {highest_name}, and amount is ${highest_bid}\n ")        