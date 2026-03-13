print("Enter 4 numbers:")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
maximum = num1
if num2 > maximum:
    maximum = num2
if num3 > maximum:
    maximum = num3
if num4 > maximum:
    maximum = num4
print("The maximum number is:", maximum)