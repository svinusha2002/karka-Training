name=input("enter the name")
age=int(input("enter the age"))
if(age<16):
    print("you can't drive",name)
if(age<18):
    print("you can't vote",name)
if(age<25):
    print("you can't rent a car",name)
if(age>25):
    print("you can do anything that legal",name)

# print(f"ok,{name},how old are you?{age}")