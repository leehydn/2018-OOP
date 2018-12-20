from cs1robots import *
from super_robot import SuperRobot
import random

load_world ("./world/sort1.wld")
hubo = SuperRobot(beepers = 5, avenue=8, street=1, orientation='W')
hubo.set_trace("blue")
numArr = []

def upAndDown(sanya: Robot):
  counter = 0
  sanya.turn_right()
  while sanya.on_beeper():
    sanya.pick_beeper()
    counter += 1

    if sanya.front_is_clear():
      sanya.move()

    else:
      break;

  sanya.turn_left(); sanya.turn_left()

  while sanya.front_is_clear():
    sanya.move()
  
  sanya.turn_right()
  numArr.append(counter)

def dropNumBeeper(sanya: Robot, num: int):
  sanya.turn_left()
  sanya.drop_beeper()
  for i in range(num-1):
    sanya.move()
    sanya.drop_beeper()

  sanya.turn_left(); sanya.turn_left();
  for i in range(num-1):
    sanya.move()
  sanya.turn_left()
  

def Beepering(sanya: Robot, numArr: list):
  sanya.turn_left(); sanya.turn_left()
  for i in range(len(numArr)):
    dropNumBeeper(sanya, numArr[i])
    hubo.move()

def main():
  hubo.move()
  while hubo.front_is_clear():
    upAndDown(hubo)
    hubo.move()
  upAndDown(hubo)
  numArr.sort()
  Beepering(hubo, numArr)

main()