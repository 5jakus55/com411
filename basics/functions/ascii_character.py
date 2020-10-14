print("Program Started!")
print("Please enter an ASCII code:")
code = abs(int(input()))
low = 32
high = 126

if code in range(low,high):
    character = chr(code)
    print("The character represented by the ASCII code {} is {}.".format(code,character))
else :
  print("Invalid character!")

print("Program ended!")