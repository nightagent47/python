height= float(input("Enter height in metres: "))
weight= float(input("Enter weight in kg: "))

bmi= weight/(height*height)
print("Your BMI is",bmi)

if bmi<=18.5:
    print("Underweight")
elif bmi>= 18.6 and bmi<=25:
    print("Keep it up, You are healthy.")
elif bmi>=25.1 and bmi<=30:
    print("Consider getting a gym membership")
elif bmi>=30.1:
    print("Whale Alert")
else:
    print("Wrong height and weight values entered")