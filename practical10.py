#Write /execute simple ‘Python’ program: Merge Two Lists and Sort it
a=[]
c=[]
n1=int(input("Enter number of elements for list 1:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements for list 2:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
print("Merged list is:",new)
new.sort()
print("Sorted list is:",new)