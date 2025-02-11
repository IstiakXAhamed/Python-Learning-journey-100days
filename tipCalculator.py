total = int(input("what is the total bill?"))
print(type(total))
members = int(input("how many people are paying bills?"))
percentage=int(input("what is the tip percentage ?10,12,15?"))
tip = 0
if(percentage==10):
    tip = (total*10)/100
elif(percentage==12):
    tip= (total*12)/100
elif(percentage==15):
    tip=(total*15)/100
else:
    print("invalid tip percentage!!!")        
    
bill = total +tip
eachPay=bill/members
print(f"Each needs to pay the amount : {eachPay}")
#print("Each needs to pay the amount :"+str(eachPay))