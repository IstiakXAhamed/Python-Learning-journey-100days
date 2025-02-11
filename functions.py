fname=input("What  is your first name?\n")
lname=input("What is your last name?\n")

def format_name(firstName,lastName):
    fullName= firstName+" "+lastName
    return fullName.title()

print(format_name(fname,lname))