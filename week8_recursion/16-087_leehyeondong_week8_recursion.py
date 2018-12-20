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
  def Branching(cBch):
    dispVec = copy.deepcopy(cBch.vec)
    dispVec.size = scale * cBch.vec.size
    _width = scale * cBch.width

    lVec = dispVec.Rotated(-splitAngle/2)
    rVec = dispVec.Rotated(splitAngle/2)

    printv(lVec)
    printv(rVec)

    lBch = Branch(cBch.end, lVec, _width, color)
    rBch = Branch(cBch.end, rVec, _width, color)

    lBch.Draw(window)
    rBch.Draw(window)

    return (lBch, rBch)

  trunk = Branch(Point(canv_x/2, canv_y), Vector(Point(0, -init_len)), init_width, color)
  trunk.Draw(window)

  bchs = [trunk]
  for i in range(n):
    n_bchs = []
    for bch in bchs:
      n_bchs.extend(Branching(bch))
    bchs = n_bchs

    if i == n-1:
      for b in n_bchs:
        cir = Circle(radius=5, centerPt=b.end); cir.setFillColor("green")
        window.add(cir)

paper = Canvas(w=canv_x, h=canv_y, bgColor="skyBlue")
drawBranch(paper, 5, toRad(50))

def drawKochCurve(init_line, window, n):
  def kochCurving(lineSeg):
    oneThird = lineSeg.vec * (1/3)
    nVec = [oneThird, oneThird.Rotated(-math.pi/3), oneThird.Rotated(-2*math.pi/3)]
    lines = [LineSegment(lineSeg.start, nVec[0]), LineSegment(lineSeg.interDivPoint(1/3), nVec[1]), LineSegment(lineSeg.interDivPoint(2/3)+nVec[2].getDisp(), -nVec[2]), \
             LineSegment(lineSeg.interDivPoint(2/3), nVec[0])
            ]

    return lines

    """for i in lines:
      i.line.setBorderWidth(2)
      printv(i.vec)
      i.Draw(window)
    """

  def Drawing(lineArr):
    for i in lineArr:
      i.Draw(window)

  
  #init_line.Draw(window)
  cList = [init_line]
  kochCurving(init_line)
  for i in range(n):
    List = []
    for line in cList:
      List.extend(kochCurving(line))
    cList = List

    if i == n-1:
      Drawing(cList)

#init_line = LineSegment(Point(0, canv_y//2), Vector(Point(canv_x, 0)))
#drawKochCurve(init_line, paper, 5)

paper = Canvas(w=canv_x, h=canv_y, bgColor="skyBlue")
canv_x /= 2
canv_y /= 2

line1 = LineSegment(Point(canv_x, canv_y), -Vector(Point(canv_x, 0)))
line2 = LineSegment(Point(0, canv_y), Vector(Point(canv_x/2, -canv_y*(3 ** 0.5)/2)))
line3 = LineSegment(Point(canv_x/2, canv_y-canv_y*(3 ** 0.5)/2), Vector(Point(canv_x/2, canv_y*(3 ** 0.5)/2)))


drawKochCurve(line1, paper, 3)
drawKochCurve(line2, paper, 3)
drawKochCurve(line3, paper, 3)