def month_name(num):
    # number=int(input("enter the number"))
    if(num==1):
        return("january")
    elif(num==2):
        return("february")
    elif(num==3):
        return("march")
    elif(num==4):
        return("april")
    elif(num==5):
        return("may")
    elif(num==6):
        return("june")
    elif(num==7):
        return("july")
    elif(num==8):
        return("august")
    elif(num==9):
        return("september")
    elif(num==10):
        return("october")
    elif(num==11):
        return("november")
    elif(num==12):
        return("december")
    else:
        print("error")
num=int(input("enter the number"))
print(month_name(num))
