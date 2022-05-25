class cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
print("Format for writing complex number: a+bj.\n")
a = complex(input('Enter First number : '))
b = complex(input('Enter Second number : '))
obj=cal(a,b)
while True:
    def menu():
        x = ('0.Quit \n1. Add \n2. Sub \n')
        print(x)
    menu()
    choice = int(input('Please select one of the following : '))
    if choice == 1:
        print("Result: ",obj.add())
    elif choice == 2:
        print("Result: ",obj.sub())
    elif choice == 0:
        print('Again try one of the following')
        break
    else:
        print('Invalid option')
        break
print()
