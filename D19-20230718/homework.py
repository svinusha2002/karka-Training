# Task 1:
# Grouping Elements by Category
# Given a list of items,group them into categories using dictionar,where the keys are values are list
# of items belonging to each category.


items_list =[
    {'name':'Apple',
     'category':'fruits'},
      {'name':'Carrot',
     'category':'vegetables'},
         {'name':'banana',
     'category':'fruits'},
      {'name':'Brocoil',
     'category':'vegetables'}
]

fruits=[]
vegetables=[]
for i in items_list:
        if(i["category"]=="fruits"):
               fruits.append(i["name"])
               print(fruits)
        if(i["category"]=="vegetables"):
                vegetables.append(i["name"])
                print(vegetables)

detail={fruits}
    


