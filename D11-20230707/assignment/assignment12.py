# quizz=input("are you ready for a quizz :")
# print("okey ")
# a=int(input("what is your capital of alakas? \n 1:melboune \n 2.anchorage \n 3.juneau \n"))
# num=0

# if(a==3):
#     print("that's right")
#     num= num+ 1
# else:
#     print("not right")
# b=int(input("can you store the value cat in a variable of a type in? \n 1. yes \n 2.no \n"))
# if(b==1):
#     print("sorry, cat is a string. ints can only store numbers ")
#     num = num+1
# else:
#     print("sorry, cat is a not string. ints can only store numbers")
   
# c=int(input("what is the result of 9+6/3? \n"))
# if(c==2):
#     print("That's correct!")
#     num=num+1
# else:
#     print("not correct!")
   
# print(num)
# print(f"overall,you got {num} of 3 correct \n Thanks for playing")



quizz=input("are you ready for a quizz :")
print("okey ")
def testin():
    a=int(input("what is your capital of alakas? \n 1:melboune \n 2.anchorage \n 3.juneau \n"))
    num=0
    if(a==3):
        print("that's right")
        num= num+ 1
    else:
        print("not right")
    b=int(input("can you store the value cat in a variable of a type in? \n 1. yes \n 2.no \n"))
    if(b==1):
        print("sorry, cat is a string. ints can only store numbers ")
        num = num+1
    else:
        print("sorry, cat is a not string. ints can only store numbers")
    
    c=int(input("what is the result of 9+6/3? \n"))
    if(c==2):
        print("That's correct!")
        num=num+1
    else:
        print("not correct!")
    return num
print(f"overall,you got {testin()} of 3 correct \n Thanks for playing")
