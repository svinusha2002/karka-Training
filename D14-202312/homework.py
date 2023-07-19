# detail=[
#         {"name" : "vinusha",
#          "age":  "21",
#          "place": "eathamozhy"
#          },
#         {"friend name 1": "deshosha",
#           "age":21,
#           "place":"muttom"},
#         {"friend name 2": "shalini",
#         "age": 21,
#         "place":"vadasey",
#         },
#         {"friend name3":"shiva gayathiri",
#         "age": 21,
#         "place":"kottar"}]
# def detail_name():
#     print("I am",detail[0]["name"],",i am",detail[0]["age"],"years old","and I'm from",detail[0]["place"])
#     print("I am",detail[1]["friend name 1"],",i am",detail[1]["age"],"years old","and I'm from",detail[1]["place"])
#     print("I am",detail[2]["friend name 2"],"i am",detail[2]["age"],"years old","and I'm from",detail[2]["place"])
#     print("I am",detail[3]["friend name3"],"i am",detail[3]["age"],"years old","and I'm from",detail[3]["place"])
# detail_name()

    
detail = [    
          {"name": "vinusha",
            "age": 18,
           "place": "eathamozhy"
           },
          {"name": "deshosha",
            "age": 20,
              "place": "muttom"
              }, 
          {"name": "shalini",
            "age": 22,
              "place": "vadasey"
              },
          {"name": "shiva gayathiri",
            "age": 21,
              "place": "kottar"
              }]
          
def data_loop():  
   for item in detail:
       if(item["age"] >21):
           print("I am", item["name"], ", I am", item["age"], "years old and I'm from", item["place"])
           
data_loop()
