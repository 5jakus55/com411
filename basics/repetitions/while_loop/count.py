live_cables = 0
print("How many live cables must I avoid?")
response = int(input())
print()  
while (live_cables < response ):

    live_cables = live_cables + 1
    print("Avoiding...Done! {} live cable avoided!".format(live_cables))
print()
print("All live cables have been avoided.")