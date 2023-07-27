


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

# print(consumer_data)
c=str(detail)
print(c)
data= input("enter the value :")
if(data=="dict"):
     file=open("/home/vinusha/Pictures/dictionary.txt","w")
     file.write(c)
     file.close()
elif(data=="string"):
     file=open("/home/vinusha/Pictures/dictionary.txt","w")
     file.write(c)
     file.close()






