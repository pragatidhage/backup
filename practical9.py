#Using List: Write a programs to:
#Create a list, add element to list, delete element from the list.
#Sort the list, reverse the list and counting elements in a list.

lst = []
# number of elements as input
n = int(input("Enter number of elements u want in list: "))
# iterating till the range
for i in range(0, n):
     ele = int(input("Enter the Number :"))
     lst.append(ele)  # adding the element
print("The list u have created is :",lst)

print("1.add element in list")
print("2.remove element from list")
print("3.sort element in list")
print("4.reverse element in list")
print("5.count element in list")

q=int(input("what do u want to do with list?:"))

if q==1:
    p=int(input("Enter the position at which u want to insert the element:" ))
    insert=int(input("Enter the element You want to insert:"))
    lst.insert(p,insert)
    print ("list after adding element is:",lst)
elif q==2:
    p = int(input("Enter the position at which u want to Delete the element:"))
    lst.remove(p)
    print("list after deleting the element is :",lst)
elif q==3:
    lst.sort()
    print("list after sorting the element is :",lst)
elif q==4:
    lst.reverse()
    print("list after reversing the element is :",lst)
elif q==5:
   ele=int(input("Enter element which u want to count :"))
   count= lst.count(ele)
   print ("The elements presents ",count,"times in list")



