dup_val=[1,2,3,2,5,1,5]
empty=[]
for i in dup_val:
    if i not in empty:
        empty.append(i)
print(empty)
    

import json
aaa={"name":"vinusha",
     "age":21,
     "place":"vellamodivilai",
     "district":"kanyakumari"}

print(json.dumps(aaa))