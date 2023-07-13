gender=input("what is your gender male or female \n")
first_name=input("enter the name \n")
last_name=input("enter the last name \n")
age=int(input("enter the age \n"))
married=input(f"are you married {first_name} (y or n)? \n")
if(gender=="male"):
    if(age>20):
        print(f"MR{last_name}")
    elif(age<20):
        print(f"{first_name}{last_name}")
elif(gender=="female"):
    if(age>20):
        if(married=="yes"):
            print(f" shall i call mrs {last_name}")
        elif(age<20):
            if(married=="no"):
              print(f"shall i call miss{last_name}")


