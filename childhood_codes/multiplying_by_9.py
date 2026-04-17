answer = input("enter a number from 1 to 10 ")
try:
  number = int(answer)
except ValueError:
  raise ValueError("it's not a number")

if number not in range(1, 11):
  raise ValueError("number is less than 1 or greater than 10")

first = str(number - 1)
second = str(10 - number)
print(first + second)

