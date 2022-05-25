#Functions : Write a program to :
#To calculate average, mean, median, and standard deviation of numbers in a list
data = []
# number of elements as input
n = int(input("Enter number of elements u want in list: "))
# iterating till the range
for i in range(0, n):
     ele = int(input("Enter the Number :"))
     data.append(ele)  # adding the element
print("The list u have created is :",data)
def mean(data):
    n = len(data)
    mean = sum(data) / n
    return mean

def my_median(data):
   n = len(data)
   index = n // 2
   # Sample with an odd number of observations
   if n % 2:
         return sorted(data)[index]
     # Sample with an even number of observations
   return sum(sorted(data)[index - 1:index + 1]) / 2


def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance


def stdev(data):
    import math
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

print("Mean of the data is % s " % (mean(data)))
print("Median of the data is % s " % (my_median(data)))
print("Standard Deviation of the data is % s " % (stdev(data)))
