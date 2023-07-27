n=int(input("enter the number"))
# for n in range(1,7):
for i in range(n):
       print("*"*n)
for i in range(n):
    for j in range(n):
         print("*",end="")
    print("")

a=int(input("enter the number :"))
sum=1
for i in range(a):
    for j in range(a):
           print(sum,end=" ")
           sum +=1
    print("")
for i,j in range(a):
        print(sum,end=" ")
        sum +=1
print("")
n=5
for i in range(1,(n*n)+1):
       print(i,end=" ")
       if(i%n==0):
        print("")


for i in range(n*n,0,-1):
        if(i%n==0):
         print("")
        print(i,end=" ")

from datetime import datetime
data_str="24 december 2022"
c=datetime.strptime(data_str,"%d %B %Y")
# print(c)
# a=type(data_str)
# print(a)
end_date=datetime.date(days=5)
print(end_date)

