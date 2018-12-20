from L9_Line import *

class HalfLine(Line):
    def __init__(self, fr, to):
        Line.__init__(self, (fr,to))
        self.__fr = fr
        self.__to = to

    def __str__(self):
        return Line.__str__(self) + "  /  " + \
               self.__fr.__str__() + "->" + self.__to.__str__()

    def contain(self, p):
        if Line.contain(self,p):
            if self.vertical():
                return (self.__to.y-self.__fr.y) * (p.y-self.__fr.y) >= 0
            return (self.__to.x-self.__fr.x) * (p.x-self.__fr.x) >= 0
        return False

    def __eq__(self, l):
        if Line.__eq__(self,l):
            return self.__fr == l.__fr and self.contain(l.__to)
        return False

    def intersection(self, l):
        pt = Line.intersection(self,l)
        if type(pt) == Point:
            if self.contain(pt) and l.contain(pt):
                return pt
            return 'none'

        if pt == 'parallel':
            return 'none'

        if self.__fr == l.__fr :
            if self.contain(l.__to):
                return 'infinitely many'
            return self.__fr

        if self.contain(l.__fr) or l.contain(self.__fr):
            return 'infinitely many'

        return 'none'

def test():
    T, F = True, False

    # test contain
    inputs = [
        [HalfLine(Point(-1,3), Point(4,-2)), Point(1,2)],
        [HalfLine(Point(-1,3), Point(4,-2)), Point(1,1)],
        [HalfLine(Point(-1,3), Point(4,-2)), Point(6,-4)],
        [HalfLine(Point(-1,3), Point(4,-2)), Point(-2,4)],
        [HalfLine(Point(4,-2), Point(-1,3)), Point(-2,4)],
        [HalfLine(Point(4,-2), Point(-1,3)), Point(6,-4)],
        [HalfLine(Point(1,1), Point(1,-3)), Point(1,-1)],
        [HalfLine(Point(1,1), Point(1,-3)), Point(1,-5)],
        [HalfLine(Point(1,1), Point(1,-3)), Point(1,3)],
        [HalfLine(Point(1,-3), Point(1,1)), Point(1,-1)],
        [HalfLine(Point(1,-3), Point(1,1)), Point(1,-5)],
        [HalfLine(Point(1,-3), Point(1,1)), Point(1,3)],
        [HalfLine(Point(1,1), Point(-3,1)), Point(-5,1)],
        [HalfLine(Point(1,1), Point(-3,1)), Point(3,1)],
        [HalfLine(Point(-3,1), Point(1,1)), Point(3,1)],
        [HalfLine(Point(-3,1), Point(1,1)), Point(-5,1)]
    ]
    outputs = [ F, T, T, F, T, F, T, T, F, T, F, T, T, F, T, F ]
    result = []
    for i in range(len(inputs)):
        result.append(inputs[i][0].contain(inputs[i][1]))
    if result == outputs:  print("HalfLine.contain(): Correct")
    else:  print ("HalfLine.contain(): NOT correct !!")

    # test ==
    inputs = [
        [HalfLine(Point(0,2),Point(2,0)), HalfLine(Point(0,2),Point(1,1))],
        [HalfLine(Point(0,2),Point(1,1)), HalfLine(Point(0,2),Point(2,0))],
        [HalfLine(Point(0,0),Point(2,2)), HalfLine(Point(0,0),Point(2,3))],
        [HalfLine(Point(0,0),Point(2,2)), HalfLine(Point(0,0),Point(-2,-2))],
        [HalfLine(Point(0,0),Point(2,2)), HalfLine(Point(1,1),Point(2,2))],
        [HalfLine(Point(1,1),Point(2,2)), HalfLine(Point(0,0),Point(2,2))],
        [HalfLine(Point(0,0),Point(2,2)), HalfLine(Point(2,2),Point(0,0))],
    ]
    outputs = [ T, T, F, F, F, F, F ]
    result = []
    for i in range(len(inputs)):
        result.append(inputs[i][0] == inputs[i][1])
    if result == outputs:  print ("HalfLine.__eq__(): Correct")
    else:  print ("HalfLine.__eq__(): NOT correct !!")

    # test intersection
    inputs = [
        [HalfLine(Point(0,2),Point(2,0)), HalfLine(Point(0,3),Point(2,1))],
        [HalfLine(Point(0,2),Point(2,0)), HalfLine(Point(3,-1),Point(4,-2))],
        [HalfLine(Point(0,2),Point(2,0)), HalfLine(Point(-2,4),Point(-1,3))],
        [HalfLine(Point(2,0),Point(0,2)), HalfLine(Point(4,-2),Point(3,-1))],
        [HalfLine(Point(2,0),Point(0,2)), HalfLine(Point(-1,3),Point(-2,4))],
        [HalfLine(Point(2,0),Point(0,2)), HalfLine(Point(2,0),Point(3,-1))],
        [HalfLine(Point(2,0),Point(3,-1)), HalfLine(Point(2,0),Point(0,2))],
        [HalfLine(Point(2,0),Point(0,2)), HalfLine(Point(1,1),Point(3,-1))],
        [HalfLine(Point(1,1),Point(3,-1)), HalfLine(Point(2,0),Point(0,2))],
        [HalfLine(Point(2,0),Point(0,2)), HalfLine(Point(3,-1),Point(4,-2))],
        [HalfLine(Point(3,-1),Point(4,-2)), HalfLine(Point(2,0),Point(0,2))],
        [HalfLine(Point(2,0),Point(2,2)), HalfLine(Point(2,-2),Point(2,-1))],
        [HalfLine(Point(2,2),Point(2,0)), HalfLine(Point(2,-2),Point(2,-3))],
        [HalfLine(Point(2,0),Point(2,2)), HalfLine(Point(2,0),Point(2,-1))],
        [HalfLine(Point(2,0),Point(2,-1)), HalfLine(Point(2,0),Point(2,2))],
        [HalfLine(Point(2,0),Point(2,2)), HalfLine(Point(2,4),Point(2,3))],
        [HalfLine(Point(2,0),Point(2,2)), HalfLine(Point(2,1),Point(2,-1))],
        [HalfLine(Point(2,4),Point(2,3)), HalfLine(Point(2,0),Point(2,2))],
        [HalfLine(Point(2,1),Point(2,-1)), HalfLine(Point(2,0),Point(2,2))],
        [HalfLine(Point(2,0),Point(2,2)), HalfLine(Point(2,-1),Point(2,-2))],
        [HalfLine(Point(2,-1),Point(2,-2)), HalfLine(Point(2,0),Point(2,2))],
        [HalfLine(Point(0,0),Point(2,2)), HalfLine(Point(0,6),Point(1,5))],
        [HalfLine(Point(0,0),Point(2,2)), HalfLine(Point(2,0),Point(3,-1))],
        [HalfLine(Point(0,0),Point(2,2)), HalfLine(Point(-2,0),Point(0,-2))],
        [HalfLine(Point(0,0),Point(2,2)), HalfLine(Point(0,-2),Point(2,-4))],
    ]
    outputs = [
        "none", "infinitely many", "infinitely many", "infinitely many",
        "infinitely many", Point(2,0), Point(2,0), "infinitely many",
        "infinitely many", "none", "none", "infinitely many", "infinitely many",
        Point(2,0), Point(2,0), "infinitely many", "infinitely many",
        "infinitely many", "infinitely many", "none", "none", Point(3,3),
        "none", "none", "none" ]
    result = []
    for i in range(len(inputs)):
        result.append(inputs[i][0].intersection(inputs[i][1]))
    if result == outputs:  print ("HalfLine.intersection(): Correct")
    else:  print ("HalfLine.intersection(): NOT correct !!")

test()
