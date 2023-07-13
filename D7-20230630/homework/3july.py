# name = input("enter the name :")
# age=input("enter the age :")
# DOB=input("enter the DOB :")
# location=input("enter the location:")
# college_name=input("enter the college name :")
# # (1) print
#print("Hello,my name is",name , ". I am ",age," years old and was born on ",DOB,". currently , I am located in",location,"and i completed my degree at",college_name)

#home work 2
age=int(input("enter the age:"))
if(age >= 18):
     print(" vote for eligible")
else:
     print("vote for not eligible")

# #home work3

a = int(input("emter the number :"))
if(a % 2 != 0):
    print("number is odd")
else:
  print("number is even")

#home work 4

item_1=int(input("enter the item1 :"))
item_2=int(input("enter the item2 :"))
item_3=int(input("enter the item3  :"))
item_4=int(input("enter the item4 :"))
total=(item_1+item_2+item_3+item_4)
print(total)
if(total >= 1000):
    print("user owned a Golden token")
elif((total >= 500) and (total < 1000)):
    print("user owned a silver token")






