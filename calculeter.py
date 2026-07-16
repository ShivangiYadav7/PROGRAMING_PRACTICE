a = float(input("enter first num:"))
b =float(input("enter scond num:"))
c=input("enter operater(+ ,-,*,/,%):")
if c =="+":
    num= a+b
    print(num)
elif c=="-":
    num= a-b
    print(num)
elif c=="*":
    num= a*b
    print(num)
elif c=="/":
    if b!=0:
        num=a/b
        print(num) 
elif c=="%":
    num=a%b   
    print(num)
else:
    print("not exist num")


