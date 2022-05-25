a=5
b=5
c=0
try:
      print(a+b)
      print(b/c)
except (TypeError,ZeroDivisionError):
      print("Invalid input")