#Write /execute simple ‘Python’ program: Remove the Duplicate Items from a List
a=[]
n=int(input("Enter number of elements for list :"))
for i in range(0,n):
    ele=int(input("Enter element:"))
    a.append(ele)
print("The list u have created is :",a)

dup_items=set()
uniq_items=[]
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print("The list after removing the duplicates :")
print(uniq_items)