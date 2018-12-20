"""def add_bar(key):
  def setDecorator(func):
    def wrapper(name):
      return "<{0}>{1}</{0}>".format(key, func(name))
    return wrapper
  return setDecorator

@add_bar("you")
def printing(name):
  return "HELLO {}".format(name)


print(printing("df"))
"""

import time
from Vector import *

class Branch:
  def __init__(self, start, vec, width, color):
    self.start = start
    self.end = Point(start.getX() + vec.getX(), start.getY() + vec.getY())
    self.vec = vec
    midPoint = Point(start.getX() + vec.getX()/2, start.getY() + vec.getY()/2)
    self.branch = Rectangle(w=width, h=self.vec.size, centerPt=midPoint)
    self.width = width
    self.branch.setBorderColor('black'); self.branch.setFillColor(color)
    self.branch.rotate(90 + 180 * self.vec.angle / math.pi)

  def Draw(self, canvas):
    canvas.add(self.branch)

scale = 0.75
canv_x = 800
canv_y = 800
init_len = 200
init_width = 10
bColor = "burlywood4"

def drawBranch(window, n, splitAngle, color=bColor):
  def Branching(n, cBch):
    if n > 0:
      dispVec = copy.deepcopy(cBch.vec)
      dispVec.size = scale * cBch.vec.size
      _width = scale * cBch.width

      lBch = Branch(cBch.end, dispVec.Rotated(-splitAngle/2), _width, color)
      rBch = Branch(cBch.end, dispVec.Rotated(splitAngle/2), _width, color)

      lBch.Draw(window)
      rBch.Draw(window)

      Branching(n-1, lBch) 
      Branching(n-1, rBch)

  trunk = Branch(Point(canv_x/2, canv_y), Vector(Point(0, -init_len)), init_width, color)
  trunk.Draw(window)

  Branching(n, trunk)

#paper = Canvas(w=canv_x, h=canv_y, bgColor="skyBlue")
#drawBranch(paper, 5, toRad(50))

def drawKochCurve(window, n, init_line):
  def DrawCurve(lineArr):
    for i in lineArr:
      try:
        i.Draw(window)
      except ValueError:
        continue

  lines = []
  def kochCurve(n, *lineArr): 
    global lines
    if n > 0:
      for line in lineArr:
        oneThird = line.vec * (1/3)
        nVec = [oneThird, oneThird.Rotated(-math.pi/3), oneThird.Rotated(-2*math.pi/3)]
        lines = [LineSegment(line.start, nVec[0]), 
                 LineSegment(line.interDivPoint(1/3), nVec[1]), 
                 LineSegment(line.interDivPoint(2/3)+nVec[2].getDisp(), -nVec[2]), 
                 LineSegment(line.interDivPoint(2/3), nVec[0])
                ]
      return list(map(kochCurve, [n-1]*4, lines))

    else:
      DrawCurve(lines)

  kochCurve(n, init_line)

#init_line = LineSegment(Point(0, canv_y//2), Vector(Point(canv_x, 0)))
#drawKochCurve(init_line, paper, 5)

canv_x = 900
canv_y = 900
paper = Canvas(w=canv_x, h=canv_y, bgColor="skyBlue")


line1 = LineSegment(Point(2*canv_x/3, 2*canv_y/3), -Vector(Point(canv_x/3, 0)))
line2 = LineSegment(Point(canv_x/3, 2*canv_y/3), Vector(Point(canv_x/6, -canv_y*(3 ** 0.5)/6)))
line3 = LineSegment(Point(canv_x/2, 2*canv_y/3-canv_y*(3 ** 0.5)/6), Vector(Point(canv_x/6, canv_y*(3 ** 0.5)/6)))

drawKochCurve(paper, 3, line1)
drawKochCurve(paper, 4, line2)
drawKochCurve(paper, 4, line3)