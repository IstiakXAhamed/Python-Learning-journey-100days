import os 
import logo

#functions for calculator 
def add(n1,n2):
    return n1+n2

def subt(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def mod(n1,n2):
    return n1%n2

operations = {
    "+":add,
    "-":subt,
    "*":mult,
    "/":div,
    "%":mod,  
}
def calculator():
    print(logo.logoC)
    shouldContinue = True
    num1 = float(input("What's the first number: "))
    while shouldContinue:

        for sign in operations:
            print(sign)
        operation_symbol = input("Pick an operation from the line above: ")
        num2=float(input("Input the number ?"))
        calculation_function=operations[operation_symbol]
        Answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {Answer}")
        num1=Answer
        
        fCalculation = input(f"Type y if u want to continue calculation with {Answer} or Type new for new calculation?")
        if(fCalculation=="y"):
           shouldContinue = True
        elif(fCalculation=="n"):
            shouldContinue = False
        elif(fCalculation=='new'):
            shouldContinue== True
            os.system('cls')
            calculator()
calculator()
        