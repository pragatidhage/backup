#Write /execute simple ‘Python’ program: Exchange the Values of Two Numbers without Using a Temporary Variable
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
a=a+b
b=a-b
a=a-b
print("a is:",a," b is:",b)