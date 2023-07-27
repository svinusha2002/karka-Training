# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# if(a>b):
#     if(a>c):
#         print("a is greater than b and c")
#     else:
#        print("a is greater")
# elif(b>c):
#      print("c is greater")
# else:
#      print("c is greater than c and a")



# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# sum=0
# if(a>sum):
#     sum=a
# if(b>sum):
#      sum=b  
# if(c>sum):
#     sum=c
# print(sum)



month_gold_rate=[{"month":"january",
                  "rate":2500},
                  {"month":"febuary",
                  "rate":5000},
                  {"month":"march",
                  "rate":3000},
                  {"month":"april",
                  "rate":2000},]
sum=month_gold_rate[0]["rate"]
sum1=0
for i in month_gold_rate:
    if(i["rate"]<sum): 
            a=i["month"]
            sum=i["rate"]  
    if(i["rate"]>sum1): 
            b=i["month"]
            sum1=i["rate"]  
      
print(f"{a} and the rate is {sum}")
print(f"{b} and the rate is {sum1}")




    