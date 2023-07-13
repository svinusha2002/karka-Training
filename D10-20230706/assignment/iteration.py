number_of_list=[250,900,456,567,345]
sum=0
for list in number_of_list:
    sum=sum+list
    print(sum)
average=sum/len(number_of_list)
print(average)
cost_of_list=[100,200,300,400,500]
empty=[]
for cost in cost_of_list:
    inr=("INR"+str(cost))
    empty.append(inr)
    print(empty)




marks=[96,72,80,67,82]
tot_marks=0
for mark in marks:
    print("before",tot_marks)
    tot_marks=tot_marks+mark
print("after",tot_marks)
enum_marks=enumerate(marks)
print(type(enum_marks))
for i,mark in enum_marks:
    print("entering iteration process for item#:",str(i))
    print("before sum",tot_marks)
    tot_marks=tot_marks+mark
    print("after sum",tot_marks)
    print("entering iteration process for item:",str(i))
    print("\n")


    
