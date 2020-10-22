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
    
  response = int(input())
  return menu[response]

def run():
  route=[]
  print( "Working out escape route...")
  for count in range(5):
    direction=menu()
    route.append(direction)
    
  print( "Escape route: {}".format(route))

run()