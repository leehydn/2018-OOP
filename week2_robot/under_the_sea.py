from cs1robots import *
from super_robot import SuperRobot
import random

load_world ("./world/sea1.wld")
hubo = SuperRobot(beepers = 5, street=9, avenue=1)
hubo.set_trace("blue")

treasureList = []

def inspectTreasure(sanya: Robot):
  counter = 0
  while 1:  
    if sanya.on_beeper():
      sanya.pick_beeper()
      counter += 1
    else:
      break;
  treasureList.append(counter)

  for i in range(counter):
    sanya.drop_beeper()
    
hubo.move(); hubo.move()
hubo.turn_right()
while hubo.front_is_clear():
  hubo.move()

hubo.turn_left() #he's now under the sea!

length = 0

while hubo.front_is_clear():
  length += 1
  hubo.move()
  inspectTreasure(hubo)

worth = treasureList.index(max(treasureList))
hubo.turn_left(); hubo.turn_left()
for i in range(length - worth -1):
  hubo.move()

for i in range(max(treasureList)):
  hubo.pick_beeper()

for i in range(worth + 1):
  hubo.move()

hubo.turn_right()

while hubo.front_is_clear():
  hubo.move()
hubo.turn_left()
hubo.move(); hubo.move(); 

for i in range(max(treasureList)):
  hubo.drop_beeper()

hubo.turn_left(); hubo.turn_left();
hubo.move()

