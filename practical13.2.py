#To read age of 15 person and count total Baby age, School age and Adult age.
count=0
count_b=0
count_s=0
count_a=0
while(count<15):
	age = int(input(" enter  age:"))
	if age <= 0:
		print('Invalid input')
	elif age >= 1 and age <= 5:
		count_b=count_b+1
	elif age >= 6 and age <= 10:
		count_s = count_s + 1
	else:
		count_a = count_a + 1
	count=count+1
print("numbers of babies:",count_b)
print("numbers of teenagers:",count_s)
print("numbers of adults:",count_a)