#Q 1. print even numbers from 1 to 20
i=1
while i<=20:
    if i%2==0:
        print(i,"even number")
    i+=1    

#Q2. print odd numbers from 1 to 20
i=1
while i<=20:
    if i%2==1:
       print(i,"odd number")
    i+=1   

#3 print the multiplication of 3
i=1
while i<=10:
    print(i*3)
    i+=1    

#Q4.   print this pattern
#*
# **
# ***
# ****
# ******

i=1
while i<=5:
    print(i*"*")
    i+=1
# Q5.  Print this pattern
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
i=1
while i<=5:
    j=1
    while j<=i:
        print(i*j ,end=" ")
        j+=1
    print() 
    i+=1