from pprint import pprint
month_gold_rate=[{"month":"january",
                  "rate":2500,
                  "jwelcost":[{"name":"ring",
                               "makingcost":14},

                               ]},
                  {"month":"febuary",
                  "rate":5000,
                  "jwelcost":[{"name":"bangle",
                              "makingcost":17},
                              ]},
                  {"month":"march",
                  "rate":3000,
                  "jwelcost":[{"name":"bracelet",
                               "makingcost":13}     
                              ]},
                 {"month":"april",
                  "rate":3000,
                  "jwelcost":[{"name":"chain",
                               "makingcost":13} 
                              ]}]
data=[]
for i in month_gold_rate:
    detail={}
    for a in i["jwelcost"]:
        new=i["month"]
        new_rate=i["rate"]
        cost=a["name"]
        total_making_cost=i["rate"]*a["makingcost"]/100
        final_amount=total_making_cost+i["rate"]
        print(f"month : {new}\n goldrate:{new_rate}\n {cost} {final_amount} \n")
        detail["month"]=new
        detail["rate"]=new_rate
        detail["name"]=cost
        detail["final_amount"]=final_amount
        data.append(detail)
pprint(data)
        # print(detail)

    

        
