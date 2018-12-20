from cs1robots import *
from super_robot import SuperRobot
import random

load_world ("./world/yardwork2.wld")
hubo = SuperRobot(beepers = 5)
hubo.set_trace("blue")
numTrash = 0

def collectTrash(sanya: Robot):
  global numTrash
  while 1:
    if sanya.on_beeper():
      sanya.pick_beeper()
      numTrash += 1
    else:
      break

def moveCollect(sanya: Robot):
  collectTrash(sanya)
  sanya.move()

column = 0
position = -1 # 1 for right, -1 for left

while hubo.front_is_clear():
  column += 1
  moveCollect(hubo)
position *= -1

def traverseMove():
  global position
  for i in range(column):
    moveCollect(hubo)
  position *= -1

def cornering():
  if not hubo.front_is_clear():
    if position == -1:
      hubo.turn_right()
      if hubo.front_is_clear():
        moveCollect(hubo)
      hubo.turn_right()

    else:
      hubo.turn_left()
      if hubo.front_is_clear():
        moveCollect(hubo)
      hubo.turn_left()

def notEnd(sanya: Robot):
  global position
  if position == 1:
    if (not hubo.left_is_clear()) and (not hubo.front_is_clear()):
      collectTrash(sanya)
      return False
  
  else:
    if (not hubo.right_is_clear()) and (not hubo.front_is_clear()):
      collectTrash(sanya)
      return False
    
  return True

def comeBackHome(sanya: Robot, cnt):
  global position
  if position == 1:
    sanya.turn_left()
    sanya.turn_left()
    traverseMove()

  sanya.turn_left()
  for i in range(cnt):
    sanya.move()
  sanya.turn_left()
    

# #######################

def main():
  cnt = 0
  while notEnd(hubo):
    cornering()
    traverseMove()
    cnt += 1
  comeBackHome(hubo, cnt)
  for i in range(numTrash):
    hubo.drop_beeper()

main()


