import matplotlib.pyplot as plt
import random as rnd

def data():
  paths={}
  print("What type of line would you like (:, -- , -)?")
  line =  input()
  print("What colour would you like (r, g, b)?")
  colour =  input()
  print("What style of marker would you like (o, s, ^)?")
  marker =  input()
  paths['line']=line
  paths['colour']=colour
  paths['marker']=marker

  return paths

def generate():
  print( "How many lines would you like to display?")
  display_lines = int(input())
  for display_line in range(display_lines):
    values = data()
    x = rnd.sample(range(1, 10), 5)
    y = rnd.sample(range(1, 10), 5)
    format = f"{values['colour']}{values['line']}{values['marker']}"
    plt.plot(x, y, format)

  plt.show()

def run():
  print("Running....")
  generate()
  print("Done!")

run()
  
