weight = int(input("Enter weight: "),10)
height = int(input("Enter height: "),10)
bmi = (weight/(height**2))*703
if(bmi < 18.5):
    print("underweight")
if(bmi > 18.5 and bmi < 24.9):
    print("normal")
if(bmi < 29.5 and bmi > 25.0):
    print("overweight")
if(bmi >= 30):
    print("obese")
