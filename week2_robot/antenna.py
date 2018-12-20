from cs1robots import *
from super_robot import SuperRobot
import random

#n = random.randint(5,10)
#m  = random.randint(5,10)
#create_world(avenues =n , streets =m)
load_world ("./world/antenna2.wld")
hubo = SuperRobot(beepers = 5)
hubo.set_trace("blue")

def climbBuilding():
  hubo.turn_left()
  while not hubo.right_is_clear():
    hubo.move()
  hubo.turn_right()

  hubo.move()
  hubo.drop_beeper()
  hubo.move()

  hubo.turn_right()
  while hubo.front_is_clear():
    hubo.move()

  hubo.turn_left()
"""
hubo.move()
climbBuilding()
hubo.move()
climbBuilding()
hubo.move()
climbBuilding()
hubo.move()
climbBuilding()
climbBuilding()
hubo.pick_beeper()
"""

def main():
  while not hubo.on_beeper():
    if not hubo.front_is_clear():
      climbBuilding()
    else:
      hubo.move()

main()
