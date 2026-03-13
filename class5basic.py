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