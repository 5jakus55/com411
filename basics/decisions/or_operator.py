print("What type of adventure should I have?")
adventure = input()
print()
if ( (adventure == "short") or (adventure == "scary")) :
  print("Entering the dark forest!")
elif ( (adventure == "long") or (adventure == "safe")) :
  print("Taking the safe route!")
else :print("Not sure which route to take." )