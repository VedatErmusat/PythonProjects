height = float(input("Your height: "))
weight = float(input("Your weight: "))


#  Calculate the BMI index using the formula: weight / (height * height)

bmi =  weight / (height ** 2)

if bmi <  18.5:
    print(f" Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is  {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is  {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
