from cs1robots import *
from super_robot import SuperRobot
import random

load_world ("./world/vending3.wld")
hubo = SuperRobot(beepers=100, avenue=1, street=2)
hubo.set_trace("blue")
counter = 0

def fillOneSide(sanya: Robot):
  global counter
  sanya.move()
  cnt = 0
  while 1:
    if sanya.on_beeper():
      sanya.pick_beeper()
      cnt += 1
    else:
      break

  sanya.drop_beeper(); sanya.drop_beeper()
  counter += 2 - cnt;
  sanya.turn_left(); sanya.turn_left();
  sanya.move()

def fillTwoSide(sanya: Robot):
  global counter
  sanya.turn_left()
  fillOneSide(sanya)
  fillOneSide(sanya)
  sanya.turn_right()

def main():
  length = 0
  hubo.move()
  hubo.move()
  while hubo.front_is_clear():
    length += 1
    fillTwoSide(hubo)
    hubo.move()
  fillTwoSide(hubo)

  hubo.turn_left(); hubo.turn_left();
  for i in range(length+2):
    hubo.move()
  
  for i in range(counter):
    hubo.drop_beeper()
  
  hubo.turn_left(); hubo.turn_left();
  hubo.move()

main()
