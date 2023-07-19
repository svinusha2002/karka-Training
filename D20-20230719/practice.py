# name="vinusha"
# dic_name={"Name":name}

# detail={"vinusha","vinu","abisha","abi"}
# print(detail)


file=open("/home/vinusha/Desktop/karka.txt","r")
# print(file)
# for line in file:
#     print(line)

# data=file.read()
# print(data)

file=open("/home/vinusha/Desktop/karka.txt","w")
# a=file.write("i am completed my college in dmi, \n i am intereste in develper")
# file.close()
# print(a)
# file=open("/home/vinusha/Desktop/karka.txt","r")
# data=file.read()
# print(data)

# write=open("/home/vinusha/Desktop/karka.txt","a")
file=open("/home/vinusha/Desktop/karka.txt","a")
file.write("subject: hospital management,environment\n wireless network")
file.close()

c=open("/home/vinusha/Desktop/karka.txt","r")
data=c.read()
print(data)



