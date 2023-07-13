number=int(input("enter the number "))
def find_day(day):
    if (day==1):
        return("sunday")
    elif(day==2):
        return("monday")
    elif(day==3):
        return("tuesday")
    elif(day==4):
        return("wednesday")
    elif(day==5):
        return("thursday")
    elif(day==6):
        print("friday")
    elif(day==7):
        return("sunday")
    else:
        return("error")
print("today is a",find_day(number))



    

         
     
 

