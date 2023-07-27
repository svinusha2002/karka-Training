
# #substract
num1=10
num2=5
def substract():
    number=(num1-num2)
    return number
number_is_substraction=substract()
print(number_is_substraction)
    
#    #multiplication
# def multiply(num1,num2):
#     number=(num1*num2)
#     return number
# number_is_multiplication=multiply(10,5)
# print(number_is_multiplication)

# #division
# def divide(num1,num2):
#     number=(num1/num2)
#     return number
# number_is_division=divide(10,5)
# print(number_is_division)


# def number(numb1,numb2,numb3):
#     numb2=numb1+numb3
#     if(numb2=numb1+numb2):

    #division
# def divide(num1,num2,num3):

#     if num2 == "+":

#     number = (num1/num3)
#     return number
# number_is_division=divide(10,5)
# print(number_is_division)


def add(num1,num2,num3):
  if(num2 == '+'):
   return num1+num3
  elif(num2 == '-'):
    return num1-num3
  elif(num2 == '*'):
    return num1*num3
  elif(num2 == '/'):
    return num1/num3
number_is_addition=add(10,"+",5)
print(number_is_addition) 