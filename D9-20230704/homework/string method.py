# #capitalize first letter capital letter
name_list=["  CARROT","potato","tomato","cauliflower"]
for vegetables in name_list:
    print(vegetables.capitalize())
#casefold() convert into small letter
    print(vegetables.casefold())
#count  
    print(vegetables.count("potato"))
#encode
    print(vegetables.encode())
#enwidth
    print(vegetables.endswith("r"))
#expandtabs 
name="v/ti/tn/tu"
for list in name:
    print(list.expandtabs(5))
# find
    print(vegetables.find("R"))
#  FORMAT
name="my name is{fname}"
for check_name in name:
    print(check_name.format(fname="vinusha"))

# index
    print(vegetables.index("CARROT"))
# ISALNUM check alphaticor number trur or false
    print(vegetables.isalnum())
# isalpha only alphatic is executed
    print(vegetables.isalpha())
#isacii alphatic letter
    print(vegetables.isascii())  
#isdecimal it ismay be in number 
    print(vegetables.isdecimal())  
#isdigit should be in number 5777 
print(vegetables.isdigit())
#isidentifier number not first,not space it contain false ststement
print(vegetables.isidentifier())
#islower all should be in smallletter
print(vegetables.islower())
#is numeric  4/5,90.00it is an false km,square,-2
print(vegetables.isnumeric())

# isprintable

#isspace " " only empty
print(vegetables.isspace())
#istitle first word will be capital letter and endwith smallletter "Hello"
print(vegetables.istitle())
#isupper is it is capital lettercondition istrue
print(vegetables.isupper())
# join join the word
print("#".join(vegetables))
 #ljust

 #lower convert into upper case
print(vegetables.lower())
 #isstrip

 #maketrans
 
 #partition spilt
# Y="my name is vinu"
# X=(Y.partition("name"))
# print(X)
 #replace
print(vegetables.replace("cauliflower","cucumber"))
 #upper convert lower case
print(vegetables.upper())

       
       
       
       
       
       
       
       
       
       

