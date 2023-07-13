# earth=int(input(" please enter your current earth station weight :"))
# planet=int(input("enter the number"))
# print(f"i have information for the follwing planets:\n 1.venus 2.mars 3.jupiter\n 4.satum 5.uranus 6.neptune")
# if(planet==1):
#     gravity=0.78*earth
# elif(planet==2):
#     gravity=0.39*earth
# elif(planet==3):
#     gravity=2.66*earth
# elif(planet==4):
#     gravity=1.17*earth
# elif(planet==5):
#     gravity=1.05*earth
# elif(planet==6):
#     gravity=1.23*earth
    
# print(f"your weightwould be {gravity}pounds on that planet ")

earth=int(input(" please enter your current earth station weight :"))
planet=int(input("enter the number"))
def earth_station(earth,planet):
     if(planet==1):
       gravity=0.78*earth
     elif(planet==2):
        gravity=0.39*earth
     elif(planet==3):
        gravity=2.66*earth
     elif(planet==4):
        gravity=1.17*earth
     elif(planet==5):
        gravity=1.05*earth
     elif(planet==6):
        gravity=1.23*earth
     return gravity
value = earth_station(earth,planet)
print(f"i have information for the follwing planets:\n 1.venus 2.mars 3.jupiter\n 4.satum 5.uranus 6.neptune")
print(f"your weightwould be {value}pounds on that planet ")
