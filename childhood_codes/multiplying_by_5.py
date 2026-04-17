answer = input("enter a number ")
try:
  number = int(answer)
except ValueError:
  raise ValueError("it's not a number")

if number % 2 == 0:
  first = str(number//2)
  second = "0"
else:
  first = str((number - 1)//2)
  second = "5"
print(first + second)