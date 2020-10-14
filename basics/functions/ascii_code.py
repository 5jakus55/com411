print("Program Started!")
print("Please enter a standard character:")
character = input()

if len(character) == 1 :
    ascii_value = ord(character)
    print( "The ASCII code for {} is : {}.".format(character,ascii_value))
else :
  print("Invalid character!")

print("Program ended!")