cricket_detail=[
            {"player" :"Dhoni",
             "number_of_centuries": 16,
             "half_centuries":54,
             "wicket_taken": 30,
             "hat-trick wickets":3,
             "batting_scores":[134,67,45,33]
             },
             {"player" :"Shane Watson",
             "number_of_centuries": 20,
             "half_centuries":45,
             "wicket taken": 20,
             "hat-trick wickets":3,
             "batting scores":[45,56,22,10]
             },
             {"player" :"Bravo",
             "number_of_centuries":25,
             "half_centuries":34,
             "wicket taken": 10,
             "hat-trick wickets":4,
             "batting scores":[5,34,10,20]
             },
             {"player" :"Moeen Ali",
             "number_of_centuries":5,
             "half_centuries":59,
             "wicket taken": 10,
             "hat-trick wickets":6,
             "batting scores":[15,10,23,0]
             },
             {"player" :"Brendon Mccullum",
             "number_of_centuries": 9,
             "half_centuries":34,
             "wicket taken": 10,
             "hat-trick wickets":8,
             "batting scores":[34,32,15,10]
             }]
def player_details():
        # print("check number of centuries in players")

        sum=0
        for i in cricket_detail:
           if i["number_of_centuries"]>=10:
              sum=sum+1
              print(sum)
        # print("check hat- tricks")
        for i in cricket_detail:
           if i["hat-trick wickets"] >= 5:
                 print(i["player"])

        list=0
        for largest in cricket_detail:
            for i in largest["batting scores"]:
             if(i["batting scores"]> list):
               list=list+1
               return i
print(player_details())

            
