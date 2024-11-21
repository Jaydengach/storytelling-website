#get height input from the user
height=input("Enter your height in Meters\n")


#converting the height input to interger
height=float(height)

#get the weight input from the user
weight=input("Enter your weight in kilograms\n")
#convert the weight to integers
weight=int(weight)

#calculate the BMI by dividing the weight and the height . The height is mutiplied by itself.
bmi=weight/(height**2)

if(bmi<18.5):
    print("under weight")

elif(18.5<=bmi<24):
    print("Normal weight")

elif(25<=bmi<29):
    print("over weight")
   


