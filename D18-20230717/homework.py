my_resume={"name": "vinusha",
           "email": "svinusha2019@gmail.com",
           "mobile-no":9487652338,
           "soft_skills":"decision making",
           "hard skills":"computer",
           "education_qualification":[{"qualification":"slsc",
                                      "insitute":"goverment higher school ,sundapattivilai",
                                      "passed out year":2017},                                     
                                      
                                      {"qualification":"+2",
                                      "insitute":"goverment higher school ,sundapattivilai",
                                      "passed out year":2019},
                                      {"qualification": "degree",
                                       "insitute":"DMI engineering college",
                                       "passout":2023}],
                                                                         
                                      
            "project":"smart saline level monitoring",
            "experience":[{"company name":"amphenol",
                           "role":"front and developer",
                           "duration":2.5},
                        {"company name":"samina",
                         "role":"back and developer",
                         "duration":1.0},
                         {"company name":"tech mahindira",
                          "role":"front end developer",
                          "duration":4.0}],
             "hobbies":["music","movie"],
              "personal details":{"father name":"selvakumar",
                                  "father's occupation":"noo",
                                  "languages known":["tamil","english"],
                                  "DOB":"07-03-2002",
                                  "gender":"female",
                                  "marital status":"no",
                                  "address":{"door no":"49/42 vellamodivilai",
                                             "post":"eathamozhy",
                                             "pincode":629501,}},
                                  }
# print(my_resume["personal details"]["address"])
# a=my_resume["education qualification"]
for i in my_resume:
    if i =="education_qualification"
        for a in i:
            print(a['education_qualification']['qualification'])
# b=my_resume["personal details"]["languages known"]
# for i in b:
#     print(i)
# c=my_resume["personal details"]
# for i in c:
#     print(i)
# d=my_resume["education qualification"]
# for i in d:
#     print(i["insitute"])
# g=my_resume["hobbies"]
# for i in g:
#     print(i)
# e=my_resume["personal details"]["DOB"]
# for i in e:
#     print(i)

# print(my_resume["personal details"]["DOB"])
# print(my_resume["personal details"]["gender"])


# for i in my_resume.values():
#     print(i)
# for i,j in my_resume.items():
#     print(f"key is {i},value is {j}")

# g=my_resume(["personal details"]["address"])
# print(g)

vinu=my_resume["experience"]
for i in vinu:
    print(i["company name"])
vinusha=my_resume["personal details"]
for i in vinusha:
    print(i)

