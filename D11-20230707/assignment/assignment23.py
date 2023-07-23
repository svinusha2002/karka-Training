print("ye olde keychain shoppe")
X=0
per_tax=0
sales_tax=8.25
shipping_cost=5.00
keychain_shipping_cost=1.00
def add_keychains(X):
    a=int(input((f"you have {X}keychains,how many to add ? \n")))
    # add=X+a
    print(f"you now have {a}keychains")
    return a
    
def remove_keychains(X):
    b=int(input(f"you have {X} keychains .how to remove ? \n"))
    remove=X-b
    
    print(f"you now have {remove} keychains")
    return remove

def view_order(X,sales_tax,shipping_cost,keychain_shipping_cost):
    total=X*shipping_cost+(X*keychain_shipping_cost)
    per_tax=(sales_tax*total)/100
    print(f"you have {X} keychains \n keychain cost $5.00 each \n total cost is ${per_tax}")
    return per_tax

def checkout(X,per_tax):
    name=input("what is your name : ")
    print(f"you have {X}keychains .\n keychains cost $ 5.00 each. \n total cost is $ {per_tax}.\n thanks for your order, {name}! ")

while True:
    choice=int(input("1. add keychains to order\n 2. remove keychains to order\n 3.view current order\n 4.checkout \n please enter your choice "))
    if(choice==1):
        add_keychains(X)
    elif(choice==2):
        remove_keychains(X)
    elif(choice==3):
        view_order(X,sales_tax,shipping_cost,keychain_shipping_cost)
    elif(choice==4):
        checkout(X,per_tax)
        break