print("What is your name human?")
name = input()
print()
print("How old are you (in years)?")
age = int(input())
print()
print("How tall are you (in meters)?")
height = float(input())
print()
print("How much do you weigh (in kilograms)?")
weight = int(input())
print()
bmi = (weight/height**2)
print("{}, you are {} years old and your BMI is {:.2f}.".format(name,age,bmi))
