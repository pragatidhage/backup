#Write /execute simple ‘Python’ program: Calculate the Average of Numbers in a Given List
def cal_average(user_list):
    sum_num = 0
    for t in user_list:
        sum_num = sum_num + t

    avg = sum_num / len(user_list)
    return avg
input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
# print list
print('list: ', user_list)
# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# Calculating the sum of list elements
print("The average of elements in list is = ",cal_average(user_list))