num=int(input("enter the number"))
def add_keychains():
    print("add keychains to order")

def remove_keychains():
    print("remove keychains to order")

def view_order():
    print("view current order")

def checkout():
    print("checkout")

if(num==1):
    add_keychains()
elif(num==2):
    remove_keychains()
elif(num==3):
    view_order()
elif(num==4):
    checkout()