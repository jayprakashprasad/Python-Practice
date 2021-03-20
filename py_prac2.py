# Online Python compiler (interpreter) to run Python online.
from prettytable import Prettytable
t = PrettyTable()
t.field_names=["ageee"]
t.add_row(['hello'])
print(t)

####3
# Online Python compiler (interpreter) to run Python online.
he=float(input("enter  your height in foot"))
he_in_meter=he*12/39.37

weight=int(input("enter your wieght in kg"))
BMI=weight/pow(he_in_meter,2)

print("bmi",BMI)

if BMi<25:
  print("overweight")
elif BMI<18:
    print("underweight")
else:
    print("fit")