details=[{"name":"vinusha",
        "place":"eathamozhy",
        "SSLC":{"maths": 99,
                "tamil": 88,
                "english":78,
                "social":90,
                "science":98}
        },
        {"name":"vinu",
        "place":"vellamodivilai",
        "SSLC":{"maths": 71,
                "tamil": 78,
                "english":79,
                "social":99,
                "science":89}
        },
        {"name":"vinisha",
        "place":"kanyakumari",
        "SSLC":{"maths": 100,
                "tamil": 58,
                "english":88,
                "social":60,
                "science":68}}]
for i in details:
        a=i["SSLC"]["maths"]
        b=i["SSLC"]["tamil"]
        c=i["SSLC"]["english"]
        d=i["SSLC"]["social"]
        e=i["SSLC"]["science"]
        total=a+b+c+d+e
#2nd question
        if(total/5) >90:
            print(i["name"],"elgible for mathsbiology")
        else:
            print(i["name"],"not eligible for maths biology")
#3nd question
        if(total/5) >80:
              print(i["name"],"elgible for computer science")
        else:
            print(i["name"],"not eligible for computer science")
#4th question
        if(i["SSLC"]["maths"]>98) and (total/5) >75:
             print(i["name"],"eligible for maths biology")
        else:
             print(i["name"],"not eligible for maths biology")

#5th question
        if(i["SSLC"]["maths"]>98) and (total/5) >70:
             print(i["name"],"eligible for computer science")
        else:
             print(i["name"],"not eligible for computer science")
          
        


