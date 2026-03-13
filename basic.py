# #  que 1 , fing sum and difference of two numbers from user
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# sum = a + b
# difference = a - b
# print("The sum of the two numbers is: ", sum)
# print("The difference of the two numbers is: ", difference)
# ----------------------------------------------------------------------------------------------------------------

# # que 2 , fing the last digit from user

# number = int(input("Enter a number: "))
# last_digit = number % 10
# print("The last digit of the number is: ", last_digit)
# ----------------------------------------------------------------------------------------------------------------
# # que 3 , sum of 2 digit number from user and seperate the digit and print the sum of the digit 
# # % is fro rimender division and // is for integer division#
# number = int(input("Enter a number: "))
# first_digit = number // 10
# second_digit = number % 10
# sum = first_digit + second_digit
# print("The sum of the two digits is: ", sum)

# ----------------------------------------------------------------------------------------------------------------
# que 4 , seprate out 3 digit number from user and print the sum of the digit in short code
# no = int(input("Enter a number: "))
# a = no // 100
# b = (no % 100) // 10
# c = no % 10
# sum = a + b + c
# print("The sum of the three digits is: ", sum)

# ----------------------------------------------------------------------------------------------------------------
#que 5 , sum of 5 digit number from user and print the sum of the digit in short code
# no = int(input("Enter a number: "))
# a = no // 10000
# b = (no % 10000) // 1000
# c = (no % 1000) // 100
# d = (no % 100) // 10
# e = no % 10
# sum = a + b + c + d + e
# print("The sum of the five digits is: ", sum)
# ----------------------------------------------------------------------------------------------------------------      

#que 6 , sum of 5 digit number from user and print the sum of the digit 
# no = int(input("Enter a number: "))
# a = no // 10000
# b = (no % 10000) // 1000
# c = (no % 1000) // 100
# d = (no % 100) // 10
# e = no % 10
# sum = a + b + c + d + e
# print("The sum of the five digits is: ", sum)
# print("a= ", a)
# print("b= ", b)
# print("c= ", c)
# print("d= ", d)
# print("e= ", e)
# ----------------------------------------------------------------------------------------------------------------
# #que 7 , reverse the 5 digit number from user and print the reverse order of the digit

# no = int(input("Enter a number: "))
# a = no // 10000
# b = (no % 10000) // 1000
# c = (no % 1000) // 100
# d = (no % 100) // 10
# e = no % 10
# reverse = e*10000 + d*1000 + c*100 + b*10 + a*1
# print("The reverse of the number is: ", reverse)
# # ----------------------------------------------------------------------------------------------------------------
#que 8 , sum of 9 digit and reverse it and print the sum of the digit
# no = int(input("Enter a number: "))
# a = no // 100000000
# b = (no % 100000000) // 10000000
# c = (no % 10000000) // 1000000
# d = (no % 1000000) // 100000
# e = (no % 100000) // 10000
# f = (no % 10000) // 1000
# g = (no % 1000) // 100
# h = (no % 100) // 10
# i = no % 10
# reverse = i*100000000 + h*10000000 + g*1000000 + f*100000 + e*10000 + d*1000 + c*100 + b*10 + a*1
# sum = a + b + c + d + e + f + g + h + i
# print("The sum of the digit is: ", sum)
# print("The reverse of the number is: ", reverse)
# # ----------------------------------------------------------------------------------------------------------------
#que 9 , accept the  9digit and accept the 1st and last number(in 3steps)
# no = int(input("Enter a number: "))
# a = no // 100000000
# b = (no % 100000000) // 10000000
# c = (no % 10000000) // 1000000
# d = (no % 1000000) // 100000
# e = (no % 100000) // 10000
# f = (no % 10000) // 1000
# g = (no % 1000) // 100
# h = (no % 100) // 10
# i = no % 10
# h = a + i
# print("The sum of the first and last number is: ", h)
# print("The first number is: ", a)
# print("The last number is: ", i)
# ----------------------------------------------------------------------------------------------------------------
# que 10 , accept baic salaary and calcutare gross salary where ta = 20% and da = 30% hra = 40%
# % is for percentage and * is for multiplication
basic_salary = int(input("Enter the basic salary: "))
ta = basic_salary * 0.2
da = basic_salary * 0.3
hra = basic_salary * 0.4
gross_salary = basic_salary + ta + da + hra
print("The gross salary is: ", gross_salary)
print("The ta is: ", ta)
print("The da is: ", da)
print("The hra is: ", hra)


