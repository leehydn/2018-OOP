import math
import copy
from cs1graphics import *

def toRad(ang):
  return ang * math.pi / 180

def printv(vec):
  print("Vector<{}, {}>".format(vec.getX(), vec.getY()))

class Vector:
  def __init__(self, end, start=Point(0,0)):
    self.dx = end.getX() - start.getY()
    self.dy = end.getY() - start.getY()
    self.size = math.sqrt(self.dx ** 2 + self.dy ** 2)

    try:
      self.angle = math.atan(self.dy / self.dx)

    except ZeroDivisionError:
      if self.dy > 0:
        self.angle = math.pi/2
      else:
        self.angle = -math.pi/2

  def Rotate(self, angle):
    self.dx = self.size * math.cos(self.angle + angle)
    self.dy = self.size * math.sin(self.angle + angle)
    self.angle = self.angle + angle

  def Rotated(self, angle):
    nVec = copy.deepcopy(self)
    nVec.dx = self.size * math.cos(self.angle + angle)
    nVec.dy = self.size * math.sin(self.angle + angle)
    nVec.angle = self.angle + angle
    
    return nVec

  def __add__(self, vec):
    dx = self.getX() + vec.getX()
    dy = self.getY() + vec.getY()
    return Vector(Point(dx, dy))

  def __mul__(self, scalar):
    nVec = copy.deepcopy(self)
    nVec.dx *= scalar
    nVec.dy *= scalar
    nVec.size = self.size * scalar
    return nVec

  def __rmul__(self, scalar):
    nVec = copy.deepcopy(self)
    nVec.dx *= scalar
    nVec.dy *= scalar
    nVec.size = self.size * scalar
    return nVec

  def __neg__(self):
    nVec = copy.deepcopy(self)
    nVec.dx *= -1
    nVec.dy *= -1
    nVec.angle += math.pi
    return nVec

  def getX(self):
    return self.dx

  def getY(self):
    return self.dy

  def getDisp(self):
    return Point(self.dx, self.dy)

class LineSegment:
  def __init__(self, start, vector, color="black"):
    self.start = start
    self.vec = vector
    self.end = start + self.vec.getDisp()
    self.line = Path(self.start, self.start + self.vec.getDisp())
    self.line.setBorderWidth(2)
    self.color = color

  def Draw(self, canvas):
    canvas.add(self.line)

  def interDivPoint(self, n):
    return self.start + self.vec.getDisp() * n

