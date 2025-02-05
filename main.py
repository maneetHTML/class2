height=float(input("height in m:"))
weight=float(input("weight in kg:"))
bmi=weight/(height**2)
print("your bmi",bmi )
if bmi<18.5:
 print("You are under weight")
elif bmi>=18.5 and  bmi<24.9:
 print("You are normal")
elif bmi>=25 and  bmi<29.9:
 print("you over weight")
elif bmi>=30 and  bmi<34.9:
 print("You are obese")
else:
 print("You are extremely obese")