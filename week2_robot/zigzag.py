from cs1robots import *
from super_robot import SuperRobot
import random

n = random.randint(5,10)
m  = random.randint(5,10)
create_world(avenues =n , streets =m)

hubo = SuperRobot(beepers = 5)
hubo.set_trace("blue")

hubo.turn_left()
row = 0
position = 1 # 1 for down, -1 for up

while hubo.front_is_clear():
  row += 1
  hubo.move()
position *= -1

def traverseMove():
  global position
  for i in range(row):
    hubo.move()
  position *= -1

def cornering():
  if not hubo.front_is_clear():
    if position == -1:
      hubo.turn_right()
      if hubo.front_is_clear():
        hubo.move()
      hubo.turn_right()

    else:
      hubo.turn_left()
      if hubo.front_is_clear():
        hubo.move()
      hubo.turn_left()

def notEnd():
  global position
  if position == 1:
    if (not hubo.left_is_clear()) and (not hubo.front_is_clear()):
      return False
  
  else:
    if (not hubo.right_is_clear()) and (not hubo.front_is_clear()):
      return False
    
  return True

# #######################

def main():   
  while notEnd():
    cornering()
    traverseMove()

main()

    

