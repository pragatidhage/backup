#Write /execute simple ‘Python’ program: Print all Numbers in a Range Divisible by a Given Number
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
if upper <= lower:
 print("please enter the upper range properly")
 upper = int(input("Enter upper range limit:"))

n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)