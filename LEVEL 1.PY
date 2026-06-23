#white a python program that prompts the user to input two numbers and then calculate 
#and displays their sum , different ,product(multiplication),and division


num1=int(input("enter the first num"))
num2=int(input("enter the second num"))
sum_result=num1+num2
subt_result=num1-num2
multi_result=num1*num2
division_result=num1/num2
print(sum_result,subt_result,multi_result,division_result,sep="\n")

#write a program to convert a given tempreture from celsius to eorenheit,and another 
#proram to convert fahrenheit back to celsius


celsisus=37
farenheit=(celsisus*9/5)+32
print(farenheit)

farenheit=98.6
celsisus=(farenheit-32)*5/9
print(celsisus)

#write a program that takes the length and width of a rectangle from the user and 
# calculates its area and perimeter.
#
lenth=float(input("enter lenth"))
width=float(input("enter the width"))
area=lenth*width
perimeter=2*(lenth+width)
print(f"area is:{area}")
print(f"perimeter is:{perimeter}")


#write a program to calculate the  simpale interest by taking the principal ,
# rate of interest,and time as input from the user.

principal=float(input("principal money"))
rate=float(input("enter the rate numberui"))
time=float(input("enter the time"))
simplelnterest=(principal*rate*time/100)
print(simplelnterest)
print(f"principal is {principal}")
print(f"rate is {rate}")
print(f"time is {time}")

#write a python program to determine whether a given number is even or odd.
num=50
if num%2==0:
    print("even")
else:
    print("odd")    

#write a program to check if a number is positive ,negative ,or zero.
num=int(input("enter te number"))   
if num==0:
    print("zero") 
elif num>0:
    print("positive")   
else:
    print("negative")    

#write a program to find the largest of three given numbers (a,b,c)


a=10
b=45
c=25
if a>=b and a>=c:
    print("largest number is " ,a) 
elif b>c and b>a:
    print("largest number is", b)
else:
    print('largest number is',c)

#whrite a program to check if a year entered by the user is leap year or common year

year= int(input("enter the year"))
if (year%400==0)  or (year%4==0 and year% 100!=0) :
    print(" is a leap year",year) 
else:
    print(" is a common  year", year)    

#voting eligibility

age=int(input("enter your date of birth"))
if age>=18:
    print(f"you are {age} years old  eligible to vot." )
else:
    print(f"you are noit eligible to  vote becose you are only {age} years old.")

#write a program that takes a student's marks  as input and assigns a grade 
# based on the following criteria A+ for marks>90,A for >80,B+for>70,B for>60,
# C for>40,D for>40,and F for all other marks.


marks=float(input("enter your marks"))
if marks>90:
    
    grade="A+"
elif marks>80:
    grade="A"
elif marks >70:
    grade="B+"
elif marks>60:
    grade="B"      
elif marks >50:
    grade="C"
elif marks>40:
    grade="D"
else:   
    grade="F"
print(f"your grade is:{grade}")

#multiplication tabale

#write a python program that take a number from the user and print its multiplication
#  table from 1 to 1o using for loop
num=int(input("enter the tabale"))
for i in range(1,11):
    print(num,"x",i,'=',num*i)


#write a python program that take a number from the user and print its multiplication
#  table from 1 to 1o using while loop

num= int (input("enter the number"))
i=1
while i<=10:
    print(f"{num} x {i}={num*i}")
    i=i+1





