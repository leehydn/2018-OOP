from cs1graphics import *
from math import *

def drawInnerTriangle(window, n, p1, p2, p3):
    if n > 0:
        p12 = Point(0.5 * (p1.getX() + p2.getX()),
                    0.5 * (p1.getY() + p2.getY()))
        p23 = Point(0.5 * (p2.getX() + p3.getX()),
                    0.5 * (p2.getY() + p3.getY()))
        p31 = Point(0.5 * (p3.getX() + p1.getX()),
                    0.5 * (p3.getY() + p1.getY()))
        window.add(Polygon(p12, p23, p31))
        drawInnerTriangle(window, n-1, p1, p12, p31)
        drawInnerTriangle(window, n-1, p2, p23, p12)
        drawInnerTriangle(window, n-1, p3, p31, p23)
            

def drawFractalTriangle(window, n, p1, p2, p3):
    window.add(Polygon(p1, p2, p3))
    drawInnerTriangle(window, n, p1, p2, p3)
    
canvas = Canvas(600,600)
layer = Layer()
drawFractalTriangle(layer,
                    7,
                    Point(100,500),
                    Point(500,500),
                    Point(300,100))
canvas.add(layer)