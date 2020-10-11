# Ask user for number of mountains
print("How many mountains should I display?")
mountains = int(input())

# Display mountains
print("\nDisplaying...")

for count in range(mountains):
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\

     """)
