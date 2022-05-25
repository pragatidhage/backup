#write a program to find max of three numbers
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
if a>b and a>c:
            print("Max Number Is",a)
elif b>a and b>c:
            print("Max Number Is",b)
else:
            print("Max Number Is",c)

