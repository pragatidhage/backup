a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
d=int(input("Enter Fourth Number:"))
e=int(input("Enter Fifth Number:"))
total=a+b+c+d+e
percent=(total/500)*100
print("total marks=",total,"percentage",percent)
if percent>=80:
    print("you have got grade A")
elif percent>=60:
    print("you have got grade B")
elif percent>=40:
    print("you have got grade C")
else :
    print("you have got grade D")
