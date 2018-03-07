height = int(input("Height in cm = "))
weight = int(input("Weight in kg = "))
BMI = weight / ((height * height)/10000)
print('BMI = ', BMI)
if BMI < 16:
    print('Severly underweight')
elif BMI < 18.5:
    print('Underweight')
elif BMI < 25:
    print('Normal')
elif BMI < 30:
    print('Overweight')
else:
    print('Obese')
