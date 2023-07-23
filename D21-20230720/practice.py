# dictionary_view=[{"month":1,
#                   "units consumed":100,
#                   "bill amount":200},
#                   {"month":2,
#                   "units consumed":150,
#                   "bill amount":300},
#                    {"month":3,
#                   "units consumed":300,
#                   "bill amount":1500},
#                    {"month":4,
#                   "units consumed":400,
#                   "bill amount":2000},
#                   ]
electricity_bill={"consumer":"vinusha",
                  "eb_reading":[1000,2000,3000,3500,4000]}
eb_bill=electricity_bill["eb_reading"]
consumer_data=[]
for unit in range(len(eb_bill)-1):
    unit1=eb_bill[unit]
    unit2=eb_bill[unit+1]
    unit_per_month=unit2-unit1
    print(unit_per_month)
    month=unit+1
    if(unit_per_month<100):
        
          a=unit_per_month*0
          total=unit_per_month+a
          print("month:",month)
          print("unitconsumed: ",a)
          print("billamount:",total)

    elif(100<=unit_per_month<200):
        
        a=unit_per_month*2
        total=unit_per_month+a
        print("month:",month)
        print("unitconsumed: ",a)
        print("billamount:",total)
    elif(200<=unit_per_month<500):
        
         a=unit_per_month*5
         total=unit_per_month*a
         print("month:",month)
         print("unitconsumed: ",a)
         print("billamount:",total)
         
    elif(unit_per_month<=1000):
        
         a=unit_per_month*14
         total=unit_per_month*a
         print("month:",month)
         print("unitconsumed: ",a)
         print("billamount:",total)

    detail={}
    detail["month"]=month
    detail["unitconsumed"]=a
    detail["billamount"]= total
    consumer_data.append(detail)
print(consumer_data)
c=str(consumer_data)
print(c)
file=open("/home/vinusha/Pictures/dictionary.txt","w")
file.write(c)
file.close()


# for data in consumer_data:
#     #  for i,value in data.items():
#     #     print(i,value)
#     overview=(f'The month is {data["month"]} and unit consumed {data["unitconsumed"]} and billamount {data["billamount"]} ')
#     print(overview)
    # file=open("/home/vinusha/Pictures/dictionary.txt","a")
    # file.write(overview)
    # file.close()


    # print(data["unitconsumed"])
    # print(data["billamount"])

     



