average=int(input("enter the number"))
if(average>=80):
   print("good")
elif(50<=average)and(80>average):
     print("average")
elif(35<=average)and(50>average):
     print("okey")   
elif(35>average):
    print("bad")
else:
    print("empty")

averages=[10,100,25,200,56]
for average in averages:
    if(average>=80):
       print("good")
    elif(50<=average)and(80>average):
       print("average")
    elif(35<=average)and(50>average):
        print("okey")   
    elif(35>average):
        print("bad")
    else:
        print("empty")
for i in averages:
    if(i>=80):
        break
    print(i)
for i in averages:
    if(i>90):
        continue
    print(i)
    
#function