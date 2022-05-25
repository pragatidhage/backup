#Looping: Write a program to :To print all prime numbers from 1 to
upper_value = int(input("Please, Enter the Upper Range Value: "))

print("The Prime Numbers in the range of 1 to ",upper_value," are: ")
for number in range(1, upper_value + 1):
    if number >= 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)