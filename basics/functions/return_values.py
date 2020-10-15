def sum_weights(bop,beep):
  weight = bop + beep
  return weight

def calc_avg_weight(bop,beep):
  avg_weight = bop + beep / 2
  return avg_weight

def run():
  print("What is the weight of Beep?")
  beep = float(input())
  print("What is the weight of Bop?")
  bop = float(input())
  print("What would you like to calculate (sum or average)?")
  calculate = input()
  if (calculate == "sum"):
    answer = sum_weights(bop,beep)
    print("The sum of Beep and Bop's weight is {:.2f}.".format(answer))
  elif (calculate == "average"):
    answer =calc_avg_weight(bop,beep)
    print("The average of Beep and Bop's weight is {:.2f}.".format(answer))
  else: print("I am not sure what you would like to do.")

run()

