bars = 0
print("How many bars should be charged?")
response = int(input())
print() 
while (bars < response ):

    bars = bars + 1
    batery = " █ " * bars
    print("Charging:{}".format(batery))
    print()
print()
print("The battery is fully charged.")