#Write /execute simple ‘Python’ program: Find the Sum of Digits in a Number
i=int(input("Enter Number:"))
sum=0
while(i>0):
    d=i%10
    sum = sum + d
    i = i // 10
print("sum of even digits=",sum)