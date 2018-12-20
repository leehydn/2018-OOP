from cs1robots import *
from super_robot import SuperRobot

#load_world("./world/reclamation1.wld")
load_world("./world/reclamation2.wld")

#hubo = SuperRobot("green", "E", 500, 1, 6)   #reclamation1.wld
hubo = SuperRobot("gray", "E", 500, 1, 9) #reclamation2.wld
hubo.set_trace("blue")
counter = 0

def fillDown(sanya: Robot):
  global counter;
  cnt = 0
  sanya.turn_right();
  while sanya.front_is_clear():
    sanya.move()
    sanya.drop_beeper()
    cnt += 1
  
  sanya.turn_left(); sanya.turn_left();
  for i in range(cnt):
    sanya.move()

  sanya.turn_right()
  counter += cnt;

def main():
  length = 1
  hubo.move()
  while hubo.front_is_clear():
    length += 1
    hubo.move()
    fillDown(hubo)

  hubo.turn_left(); hubo.turn_left();
  for i in range(length):
    hubo.move()
  
  for j in range(counter):
    hubo.drop_beeper();

  hubo.turn_left(); hubo.turn_left(); hubo.move();

main()
  

  


  
