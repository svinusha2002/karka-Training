print("ye olde keychain shoppe")
X=0
def add_keychains(X):
    a=int(input((f"you have {X} keychains,how many to add ? \n")))
    add=X+a
    print(f"you now have {X} keychains")
    return add
def remove_keychains(X,add):
    b=int(input(f"you have {add} keychains .how to remove ? \n"))
    remove=X-b
    
    print(f"you now have {remove} keychains")
    return remove

def view_order(X):
    rupee=2
    price=10*rupee
    print(f"you have {price} keychains \n keychain cost $10 each \n total cost is ${price}")
    return price

def checkout(X,price):
    name=input("what is your name : ")
    print(f"you have {X}keychains .\n keychains cost $ 10 each. \n total cost is $ {price}.\n thanks for your order, {name}! ")

while True:
    choice=int(input("1. add keychains to order\n 2. remove keychains to order\n 3.view current order\n 4.checkout \n please enter your choice "))
    if(choice==1):
        add_keychains(X)
    elif(choice==2):
        remove_keychains(add_keychains(X))
    elif(choice==3):
        view_order(X)
    elif(choice==4):
        checkout(X,'price')
        break