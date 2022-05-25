#Generate multiplication table up to 10 for numbers 1 to 5.
for j in range(1,6):
    print("table of ",j)
    # use for loop to iterate 10 times
    for i in range(1,11):
       print(j,'x',i,'=',j*i)