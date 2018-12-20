from cs1robots import *

class SuperRobot(Robot):

  def GiveBeeper(self, num):
    self._beeper_bag += num

  def turn_right(self):
    self._image[self._dir].moveTo(-100, -100)
    self._dir = (self._dir - 1) % 4
    self._update_pos()
    #self._update_trace()
    self._refresh()

  def turn_around(self):
    self.turn_left(); self.turn_left()