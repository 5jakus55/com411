print("Please enter the first whole number.")
first_number = int(input())
print("Please enter the second whole number.")
second_number = int(input())
print("Please enter the third whole number.")
third_number = int(input())

num_even = 0
num_odd = 0

if ( first_number % 2 == 0) :
   num_even += 1
else :
   num_odd +=1

if ( second_number % 2 == 0) :
   num_even += 1
else :
   num_odd +=1

if ( third_number % 2 == 0) :
   num_even += 1
else :
   num_odd +=1 

print("There were {} even and {} odd numbers".format(num_even,num_odd))