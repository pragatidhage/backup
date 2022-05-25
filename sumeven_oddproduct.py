#write a program to find sum of even digits and product of odd digits of a given number
i=int(input("Enter Number:"))
sum=0
prod=1
while(i>0):
    d=i%10
    if d%2==0:
        sum=sum+d
    else:
        prod=prod*d
    i=i//10
print("sum of even digits=",sum,"product of digits=",prod)

