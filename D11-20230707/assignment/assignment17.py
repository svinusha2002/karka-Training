height=float(input("enter the number"))
weight=int(input("enter the weight"))
BMI=weight/(height**2)
print(f"your BMI IS {BMI }")
if(BMI<18.5):
    print("underwater")
elif(18.5 <=BMI<=24.9):
    print("normal weight")
elif(25.0<=BMI>=29.9):
    print("over weight")
elif(BMI>30.0):
    print("obese")