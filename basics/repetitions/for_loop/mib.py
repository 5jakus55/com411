print("How many miles must I travel before I reach the secret base?")
response = abs(int(input()))
print("I will count the miles...")
print()
for miles in range(response,0,-1):
  print("I have {} miles to go before I reach the base.".format(miles))
print()
print("I have arrived at the secret headquarters of the MIB!")
print("It is time to sneak in.")