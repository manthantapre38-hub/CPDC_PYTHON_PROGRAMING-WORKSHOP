# accept 4 numbers and find max number
n1 = int(input("Enter Value: "))
n2 = int(input("Enter Value: "))
n3 = int(input("Enter Value: "))
n4 = int(input("Enter Value: "))
n5 = int(input("Enter Value: "))
n6 = int(input("Enter Value: "))
n7 = int(input("Enter Value: "))
n8 = int(input("Enter Value: "))
n9 = int(input("Enter Value: "))
n10 = int(input("Enter Value: "))
n11 = int(input("Enter Value: "))

max_num = n1

if n2 > max_num:
    max_num = n2
if n3 > max_num:
    max_num = n3
if n4 > max_num:
    max_num = n4
if n5 > max_num:
    max_num = n5
if n6 > max_num:
    max_num = n6
if n7 > max_num:
    max_num = n7
if n8 > max_num:
    max_num = n8
if n9 > max_num:
    max_num = n9
if n10 > max_num:
    max_num = n10
if n11 > max_num:
    max_num = n11

print("Max number:", max_num)
 


 arr = [int(x) for x in input().split()]

print("Max:", max(arr))
print("Min:", min(arr))



# Check leap year 
year=int(input("Enter Year:"))
if year%100!=0:
   if year%4==0:
      print("Non Century leap Year")
   else:
       print("Not leap year")
else:
   if year%400==0:
      print("Century Leap year")
   else:
      print("Not leap year")      





      # Tech Number '
n0=2025
n1=nonlocal

## number 
 



year=int(input("enter value:"))
if year%100!=0:
    if year%4==0:
        print("non century leap year :")
    else:
         print("non leap year :")  
else:
    if year%400==0:
        print( "century leap year :")
    else:
         print(" leap year :")          
