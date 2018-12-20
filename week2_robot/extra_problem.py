# Task 8. Hubo Clock
# Hubo wants to build a digital clock to show current time. 

from cs1robots import *
from super_robot import SuperRobot
import time
from datetime import datetime

now = time.gmtime(time.time())  
timeList = [str(datetime.now().hour), str(now.tm_min), str(now.tm_sec)]
for i in range(3):
  if len(timeList[i]) < 2:
    temp = timeList[i]
    timeList[i] = "0" + temp

load_world("./world/myworld.wld")

hubo = SuperRobot()

def writeNumber(jay: SuperRobot, num: int):
  assert num >= 0 and num <= 9

  if num == 0:
    jay.GiveBeeper(12)
    
    jay.turn_left(); jay.drop_beeper()
    for i in range(4):
      jay.move()
      jay.drop_beeper()
      
    jay.turn_right()
    for i in range(2):
      jay.move()
      jay.drop_beeper()

    jay.turn_right()
    for i in range(4):
      jay.move()
      jay.drop_beeper()
    jay.turn_right()
    jay.move(); jay.drop_beeper(); jay.move(); jay.turn_around()
  if num == 1:
    jay.GiveBeeper(5)
    jay.move(); jay.move()
    jay.turn_left(); jay.drop_beeper()
    for i in range(4):
      jay.move()
      jay.drop_beeper()

    jay.turn_around()
    for i in range(4):
      jay.move();
    jay.turn_right()
    jay.move(); jay.move();
    jay.turn_around()
  if num == 2:
    jay.GiveBeeper(11)
    jay.move(); jay.move(); jay.turn_around()
    jay.drop_beeper(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_right()
    jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper(); 
    jay.turn_right()
    jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_left()
    jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_left()
    jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_left();

    for i in range(4):
      jay.move()
    jay.turn_left()
  if num == 3:
    jay.GiveBeeper(13)
    jay.drop_beeper(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper()
    jay.turn_left()
    jay.move(); jay.drop_beeper(); jay.move();
    jay.turn_left()
    jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper()
    jay.turn_around()
    jay.move(); jay.move(); jay.drop_beeper()
    jay.turn_left()
    jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper()
    jay.turn_left()
    jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper()
    jay.turn_left()

    for i in range(4):
      jay.move()
    jay.turn_left()
  if num == 4:
    hubo.GiveBeeper(9)
    hubo.move(); hubo.move(); hubo.turn_left()
    for i in range(4):
      hubo.drop_beeper(); hubo.move();
    hubo.drop_beeper(); hubo.turn_around()
    hubo.move(); hubo.move(); hubo.turn_right()
    hubo.move(); hubo.drop_beeper(); hubo.move(); hubo.drop_beeper();
    hubo.turn_right(); hubo.move(); hubo.drop_beeper(); hubo.move(); hubo.drop_beeper()
    hubo.turn_around()
    for i in range(4):
      hubo.move()
    hubo.turn_left()
  if num == 5:
    jay.GiveBeeper(11);
    jay.drop_beeper(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_left(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_left(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_right(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_right(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_around();
    for i in range(2):
      jay.move()
    jay.turn_left()
    for i in range(4):
      jay.move();
    jay.turn_left()
  if num == 6:
    jay.GiveBeeper(12);
    jay.drop_beeper(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_left(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_left(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_right(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_right(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper();
    jay.turn_around();
    for i in range(2):
      jay.move()
    jay.turn_left()
    for i in range(3):
      jay.move();
    jay.drop_beeper()
    jay.move()
    jay.turn_left()
  if num == 7:
    jay.GiveBeeper(9)
    jay.move(); jay.move(); jay.turn_left()
    for i in range(4):
      jay.drop_beeper(); jay.move()
    jay.turn_left()
    for i in range(2):
      jay.drop_beeper(); jay.move()
    jay.drop_beeper()
    jay.turn_left()
    for i in range(2):
      jay.move(); jay.drop_beeper()
    jay.move(); jay.move()
    jay.turn_left()
  if num == 8:
    jay.GiveBeeper(13)
    def oddFunc():
      jay.drop_beeper(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper(); jay.turn_left(); jay.move(); jay.turn_left()
    
    def evenFunc():
      jay.drop_beeper(); jay.move(); jay.move(); jay.drop_beeper(); jay.turn_right(); jay.move(); jay.turn_right()

    oddFunc(); evenFunc(); oddFunc(); evenFunc();
    for i in range(2):
      jay.drop_beeper(); jay.move(); 
    jay.drop_beeper()
    jay.turn_around()
    for i in range(2):
      jay.move()
    jay.turn_left()
    for i in range(4):
      jay.move()
    jay.turn_left()
  if num == 9:
    jay.GiveBeeper(12)
    jay.drop_beeper(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper(); jay.turn_left()
    for i in range(4):
      jay.move(); jay.drop_beeper()
    jay.turn_left(); jay.move(); jay.drop_beeper(); jay.move(); jay.drop_beeper(); jay.turn_left()
    jay.move(); jay.drop_beeper(); jay.move(); jay.turn_left(); jay.move(); jay.turn_around(); jay.drop_beeper();
    jay.move(); jay.drop_beeper();
    jay.turn_left(); jay.move();
    jay.move(); jay.turn_left()

      
def main():
  writeNumber(hubo, int(timeList[0][0])); hubo.move(); hubo.move(); hubo.move(); hubo.move();
  writeNumber(hubo, int(timeList[0][1])); hubo.move(); hubo.move(); hubo.move(); hubo.move();
  writeNumber(hubo, int(timeList[1][0])); hubo.move(); hubo.move(); hubo.move(); hubo.move();
  writeNumber(hubo, int(timeList[1][1])); hubo.move(); hubo.move(); hubo.move(); hubo.move();
  writeNumber(hubo, int(timeList[2][0])); hubo.move(); hubo.move(); hubo.move(); hubo.move();
  writeNumber(hubo, int(timeList[2][1])); hubo.move(); hubo.move()


main()

 