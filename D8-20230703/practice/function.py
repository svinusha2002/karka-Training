

def eligible_for_vote(age):
    if(age>=18):
        return("not eligible for vote")
    else:
        return("eligible for vote")
eligible_for_checking=eligible_for_vote(23)
print(eligible_for_checking)
        


def number_is(number):
    if number%2==0 :
        return("odd")
    else:
        return("even")
check_odd_even=number_is(67)
print(check_odd_even)

def calculation(p,n,r):
    interest=int((p*n*r/100))
    return interest
# p=1000
# n=100
# r=2
# interest=(p*n*r/100)
# print(interest)

def calculation(p,n,r):
    interest=int(p*n*r/100)
    return interest
checking_simple_interest=calculation(1000,100,2)
print(checking_simple_interest)

# #length
# l=len("vinusha")
# print(l)

# #lower
# my_name="vinusha"
# l=my_name.upper()
# print(l)

# def name(a): 
#     data=a
#     return data
# my_name=name("vinu")
# print(my_name)


def vegetables(potato,tomato):
    number_of_vegetable=potato,tomato
    return number_of_vegetable
check_vegetables=vegetables("potato","tomato")
print(check_vegetables)






   
      

