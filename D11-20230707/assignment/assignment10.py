# name=input("enter the name")
# age=int(input("enter the age"))
# print(f"hey,what's your name?(sorry, i keep forgetting.){name}\nok,{name},how old are you?{age}")
# if(age<16):
#      print("you can drive but not vote",name)
# if(16<=age<=17):
#     print("you can't vote",name)
# if(18<=age<=24):
#     print("you can vote but not rent a car",name)
# if(age>=25):
#     print("you can do prettymuch anything ,",name)




def vote(name,age):
  if(age<16):
     value = print("you can drive but not vote",name)
  if(16<=age<=17):
     value = print("you can't vote",name)
  if(18<=age<=24):
    value =  print("you can vote but not rent a car",name)
  if(age>=25):
    value =  print("you can do prettymuch anything ,",name)
  return value
name=input("enter the name =")
age=int(input("enter the age =" ))   
print(f"hey,what's your name?(sorry, i keep forgetting.){name}\n ok,{name},how old are you?{age}")
print(vote(name,age))

