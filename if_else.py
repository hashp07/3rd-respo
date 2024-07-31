x= int(input("enter the year: "))

if(x%400==0 and x%100==0):
    print("%d is a leap year"%x)
elif(x%4==0 and x%100!=0):
    print("%d is a leap year"%x)
else:
    print("%d is a not a leap year"%x)
