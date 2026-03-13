# no = int(input("Enter a number: "))
# rev = 0 
# while no >0:
#     rem = no %10
#     rev = rev * 10 + rem
#     no = no // 10
# print("The reverse of the number is: ", rev)
#----------------------------------------------------------------------------------------------------------------
##count number of digits in a number and sum of the digits

# no = int(input("Enter a number: "))
# count = 0
# sum = 0
# while no > 0:
#     rem = no % 10 # rem = 9
#     count = count + 1 # count = 0 + 1 = 1
#     sum = sum + rem # sum = 0 + 9 = 9
#     no = no // 10 # no = 3486
# print("The number of digits is: ", count)
# print("The sum of the digits is: ", sum)
#----------------------------------------------------------------------------------------------------------------
##check if a number is a palindrome is yes then reverse it and print the reverse number
# no = int(input("Enter a number: "))
# rev = 0 
# while no > 0:
#     rem = no % 10 # rem = 9
#     rev = rev * 10 + rem # rev = 0 * 10 + 9 = 9
#     no = no // 10 # no = 3486
# if no == rev:
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")
# print("The reverse of the number is: ", rev)

#----------------------------------------------------------------------------------------------------------------   
#ckeck arsmstrong number
no = int(input("enter the number :"))
sum = 0
temp = no
while temp > 0:
    rem = temp % 10 # rem = 9
    sum = sum + rem ** 3 # sum = 0 + 9 ** 3 = 729
    temp = temp // 10 # temp = 3486
if no == sum:
    print("The number is a armstrong numbeer")
else:
    print("The number is not a armstrong number")
    print("The sum of the number is: ", sum)
    #--------------------------------------------------------------------------------------------------------------
    #
