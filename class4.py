def add(x,y):
    res1=x+y
    res2=x+y
    res3=x+y
    return res1,res2,res3
if __name__ == '__main__':
    a=int(input("enter the value: "))
    b=int(input("enter the value: "))
    r1,r2,r3 =add(a,b)
    print(r1,r2,r3)