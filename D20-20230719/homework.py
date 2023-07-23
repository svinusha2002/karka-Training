electricity_bill={"consumer":"vinusha",
                  "eb_reading":[1000,2000,3000,3500,4000]}
eb_bill=electricity_bill["eb_reading"]
for unit in range(len(eb_bill)-1):
    unit1=eb_bill[unit]
    unit2=eb_bill[unit+1]
    unit_per_month=unit2-unit1
    print(unit_per_month)
    month=unit+1
    if(unit_per_month<100):
        
          a=unit_per_month*0
          total=unit_per_month+a
          print("month :",month)
          print("unit consumed: ",a)
          print("bill amount:",total)

    elif(100<=unit_per_month<200):
        
        a=unit_per_month*2
        total=unit_per_month+a
        print("month :",month)
        print("unit consumed: ",a)
        print("bill amount:",total)
    elif(200<=unit_per_month<500):
        
         a=unit_per_month*5
         total=unit_per_month*a
         print("month :",month)
         print("unit consumed: ",a)
         print("bill amount:",total)
         
    elif(unit_per_month<=1000):
        
         a=unit_per_month*14
         total=unit_per_month*a
         print("month :",month)
         print("unit consumed: ",a)
         print("bill amount:",total)

    detail={}
    detail["month "]=month
    detail["unit consumed"]=a
    detail["bill amount"]= total
    eb_bill.append(detail)
    print(eb_bill)

    
         







        
        
    

      
