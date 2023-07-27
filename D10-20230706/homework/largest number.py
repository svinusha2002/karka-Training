def largest_number(my_list):
    large=0
    for i in my_list:
        if(i>large):
          large=i
    return large
my_list=[250,890,500,900,300,1000]
print(largest_number(my_list))


my_list=[12,56,78,90]
list=1
for largest in my_list:
   if(largest>list):
      list=largest
print(list)
    
      