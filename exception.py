a=int(input("Enter the number to find square:"))
try:
    print(a*a)
except TypeError:
    print("Exception Occurred")

else:
    print("Try block executed successfully")