def removing_zeros(number):
  while number[0] == 0:
    number = number[1:]
    if len(number) == 0:
      return 0
  return number

def binary(dec):
  dec = removing_zeros(dec)
  if dec == 0:
    return 0
  try:
    dec = int(dec)
  except:
    raise ValueError("It's not a decimal number.")
  bin_ = ""
  n = 0
  while n >= 0 and dec > 0:
    if 2**n <= dec:
      if 2**(n+1) <= dec:
        n += 1  # Find the largest power of 2 less than the input
      else:
        while n >= 0:
          if 2**n <= dec:  # Check if 2 to the power of n is less than left decimal to convert decimal to binary
            bin_ += "1"
            dec -= 2**n
          else:
            bin_ += "0"
          n -= 1
  return(bin_)

def decimal(bin_):
  bin_ = removing_zeros(bin_)
  if bin_ == 0:
    return 0
  for b in bin_:
    if b not in ["0", "1"]:  # Binary numbers contain only zeros and ones
      raise ValueError("It's not a binary number.")
  dec = 0
  for i in range(len(bin_)):
    if bin_[i] == "1":
      dec += 2**(len(bin_)-i-1)
  return dec

def bytes(bin_):
  byt = ""
  while len(bin_)%8 != 0:
    bin_ = "0" + bin_  # The length of the binary's value has to be divisible by 8 because byte contains 8 bies
  for i in range(len(bin_)//8):  # Check bytes' number
    byt += bin_[8*i:8*(i+1)] + " "  # Take every 8 value's numbers to get full bytes
  byt = byt[:-1]
  return byt

print("Type:") # Instructions for user
print("1 to convert binary number to decimal")
print("2 to convert decimal number to binary")
print("3 to convert signs to their binary equivalent (in bytes)")
print("4 to convert signs to their decimal equivalent (based on binary ones)")
print("5 to convert decimal numbers to signs")
print("6 to convert binary number to sign (only one)") # Signs can be composed of different numbers of bytes
print("7 to convert bytes to signs (only or one-byted signs, BYTES HAVE TO BE SEPARATED BY SPACE)")
print()

def binary_to_decimal():
  return (decimal(input("Enter a binary number: ")))

def decimal_to_binary():
  return (binary(input("Enter a decimal number: ")))

def signs_to_bytes():
  signs = input("Enter a message: ")
  byt = ""
  for i in signs:
    byt += bytes(binary(str(ord(i)))) + " "
  byt = byt[:-1]
  return byt
    
def signs_to_decimal():
  signs = input("Enter a message: ")
  decimal = ""
  for i in signs:
    decimal += str(ord(i)) + " "
  decimal = decimal[:-1]
  return decimal

def decimal_to_signs():
  dec = input("Enter numbers: ").split(" ")
  signs = ""
  for i in dec:
    try:
      i = int(i)
    except:
      raise ValueError("It's not a decimal number")
    signs += str(chr(i))
  return signs

def binary_to_one_sign():
  return chr(decimal(input("Enter a binary number: ")))
  
def bytes_to_signs():
  bin_ = input("Enter bytes: ").split(" ")
  signs = ""
  for i in bin_:
    if len(i) != 8:
      raise ValueError("There is a string in value which isn't a byte, byte contains 8 bites")
    signs += str(chr(decimal(i)))
  return signs
user_menu = {
  "1": binary_to_decimal,
  "2": decimal_to_binary,
  "3": signs_to_bytes,
  "4": signs_to_decimal,
  "5": decimal_to_signs, 
  "6": binary_to_one_sign,
  "7": bytes_to_signs
}
user_answer = input("Enter the appropriate number: ")
if user_answer not in user_menu.keys():
  raise ValueError("Error, enter a number from 1 to 7")

print(user_menu[user_answer]())