def directions():
  directions=["Move Forward", 
              "Move Backward", 
              "Turn Left", 
              "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  menu = directions()
  for index in range(len(menu)):
    print("{}: {}".format(index,menu[index]))

def run():
  menu()

run()