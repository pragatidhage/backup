#Using Dictionary: Write a programs to:(i) Create dictionary, add element to dictionary, delete element from the
# dictionary
my_dict = {1: 'apple', 2: 'ball'}
print("Dictionary created is:\n",my_dict)

my_dict[3]='cat'
my_dict[4]='dog'
my_dict[5]='elephant'
print("\nAfter adding element in dictionary:\n",my_dict)

my_dict.pop(1)
print("\nAfter deleting element from dictionary:\n",my_dict)