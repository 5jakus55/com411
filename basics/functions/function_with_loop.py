def cross_bridge(steps) :
  for step in range(steps) :
    print("Crossed step.")
     
  if (steps > 5) :
    print("The bridge is collapsing!")
  else : print("We must keep going!")


cross_bridge(5)
cross_bridge(2)
cross_bridge(10)
