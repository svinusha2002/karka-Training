def my_list(a):
    for i,num in enumerate(a):
        if(num==85):
         return i
print(my_list([56,76,85,90]))


def my_friend(a):
   for friend in (a):
      if(friend=="abisha"):
         return friend
print(my_friend(["vinusha","abisha","vinu"])," is my favorite friend")
    
         

# def my_friend(friend):
#    for i,num in enumerate(friend):
#       if(num=="deshosha"):
#          return i
# print(my_friend(["vinu","deshosha","vinusha","abisha"]))


def largest_number(my_list):
    large=len(my_list[0])
    for i in my_list:
        if(len(i)>large):
          large=len(i)
        
    return i
my_list=["vinusha","vinu","abisha"]
print(largest_number(my_list))



         
         




   

