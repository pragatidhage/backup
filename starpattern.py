n= int(input("enter the number of rows:"))
#outer loop will handel number of rows
for i in range (0,n):

    #inner loop will handel number of columns
    for j in range(0,i+1):
        print("*",end="")
    #ending line after each row
    print("\r")
