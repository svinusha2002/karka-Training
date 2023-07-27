education_details=[{"study":"B.E",
                    "institute":"DMI engineering college",
                    "semester marks":[{"semester name":1,
                                       "subjects":["embedded system","principle of management","optical communication"],
                                                   "semester grade":"A",
                                                   },
                                          {"semester name":2,
                                            "subjects":["microproceesor","antenna","wirless network"],
                                            "semester grade":"A++",
                                            },
                                            {"semester name": 3,
                                             "subjects":["hospital managemengt","environment","python"],
                                             "semester":"B",
                                             }],     
                                            }]
for i in education_details:
    for a in i["semester marks"]:
        print(a["semester name"])
        b=a["semester name"]
        for name in b[0]:
            print(name)
    
# print(education_details[0])
# print(education_details["semester exam"]["semester name"])
