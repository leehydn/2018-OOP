from L9_Line import *

class LineSegment(Line):
    def __init__(self, p, q):
        Line.__init__(self, (p,q))
        self.__p = p
        self.__q = q


    def __str__(self):
        return Line.__str__(self) + "  /  " + \
               self.__p.__str__() + "-" + self.__q.__str__()

    def __eq__(self, l):
        return {(self.__p.x, self.__p.y), (self.__q.x, self.__q.y)} == \
        {(l.__p.x, l.__p.y), (l.__q.x, l.__q.y)}

    def contain(self, p):
        line = Line((self.__p, self.__q))
        if line.contain(p):
            ymin, ymax = sorted((self.__p.y, self.__q.y))
            xmin, xmax = sorted((self.__p.x, self.__q.x))
            return ymin <= p.y <= ymax and xmin <= p.x <= xmax
        return False

    def intersection(self, l):
        pt = Line.intersection(self,l)
        if type(pt) == Point:
            if self.contain(pt) and l.contain(pt):
                return pt
            return 'none'
        if pt == 'parallel':
            return 'none'

        if self.__eq__(l):
            return 'infinitely many'

        if self.__p == l.__p:
            ls = LineSegment(self.__q, l.__q)
            if ls.contain(l.__p):
                print(l.__p)
                return l.__p
            return 'infinitely many'

        if self.__q == l.__p:
            ls = LineSegment(self.__p, l.__q)
            if ls.contain(l.__p):
                return l.__p

        if self.__p == l.__q:
            ls = LineSegment(self.__q, l.__p)
            if ls.contain(l.__q):
                return l.__q
            return 'infinitely many'

        if self.__q == l.__q:
            ls = LineSegment(self.__p, l.__p)
            if ls.contain(l.__q):
                return l.__q

        if self.contain(l.__p) or self.contain(l.__q):
            return 'infinitely many'
        if l.contain(self.__p) or l.contain(self.__q):
            return 'infinitely many'
        return 'none'

    def perp_bisector(self):  # perpendicular bisector
        vec = (self.__q.x - self.__p.x, self.__q.y - self.__p.y)
        perp_vec = (vec[1], -1*vec[0])
        midPoint = Point((self.__p.x + self.__q.x)/2, (self.__p.y + self.__q.y)/2)
        pP = Point(midPoint.x + perp_vec[0], midPoint.y + perp_vec[1])

        return Line((midPoint, pP))

def test_1():
    T, F = True, False

    # test ==
    inputs = [
        [LineSegment(Point(0,0),Point(2,2)), LineSegment(Point(0,0),Point(3,3))],
        [LineSegment(Point(0,0),Point(2,2)), LineSegment(Point(0,0),Point(-2,-2))],
        [LineSegment(Point(0,0),Point(2,2)), LineSegment(Point(2,2),Point(0,0))],
        [LineSegment(Point(0,0),Point(2,2)), LineSegment(Point(0,0),Point(2,2))]
    ]
    outputs = [ F, F, T, T ]
    result = []
    for i in range(len(inputs)):
        result.append(inputs[i][0] == inputs[i][1])
    if result == outputs:  print ("LineSegment.__eq__(): Correct")
    else:  print ("LineSegment.__eq__(): NOT correct !!")

    # test contain
    inputs = [
        [LineSegment(Point(-1,3), Point(4,-2)), Point(1,1)],
        [LineSegment(Point(4,-2), Point(-1,3)), Point(1,1)],
        [LineSegment(Point(1,1), Point(1,-3)), Point(1,-1)],
        [LineSegment(Point(1,-3), Point(1,1)), Point(1,-1)],
        [LineSegment(Point(1,1), Point(-3,1)), Point(-1,1)],
        [LineSegment(Point(-3,1), Point(1,1)), Point(-1,1)],
        [LineSegment(Point(-1,3), Point(4,-2)), Point(1,2)],
        [LineSegment(Point(1,1), Point(1,-3)), Point(1,2)],
        [LineSegment(Point(1,1), Point(1,-3)), Point(1,-4)],
        [LineSegment(Point(-3,1), Point(1,1)), Point(2,1)],
        [LineSegment(Point(-3,1), Point(1,1)), Point(-4,1)]
    ]
    outputs = [T, T, T, T, T, T, F, F, F, F, F]
    result = []
    for i in range(len(inputs)):
        result.append(inputs[i][0].contain(inputs[i][1]))
    if result == outputs:  print ("LineSegment.contain(): Correct")
    else:  print ("LineSegment.contain(): NOT correct !!")

    # test intersection
    inputs = [
        [LineSegment(Point(0,2),Point(2,0)), LineSegment(Point(0,3),Point(2,1))],
        [LineSegment(Point(0,2),Point(2,0)), LineSegment(Point(3,-1),Point(4,-2))],
        [LineSegment(Point(0,2),Point(2,0)), LineSegment(Point(-2,4),Point(-1,3))],
        [LineSegment(Point(2,0),Point(0,2)), LineSegment(Point(1,1),Point(3,-1))],
        [LineSegment(Point(2,0),Point(0,2)), LineSegment(Point(3,-1),Point(1,1))],
        [LineSegment(Point(2,0),Point(0,2)), LineSegment(Point(-1,3),Point(3,-1))],
        [LineSegment(Point(2,0),Point(0,2)), LineSegment(Point(3,-1),Point(-1,3))],
        [LineSegment(Point(3,-1),Point(-1,3)), LineSegment(Point(0,2),Point(2,0))],
        [LineSegment(Point(2,0),Point(0,2)), LineSegment(Point(3,-1),Point(2,0))],
        [LineSegment(Point(3,-1),Point(2,0)), LineSegment(Point(0,2),Point(2,0))],
        [LineSegment(Point(2,0),Point(2,2)), LineSegment(Point(2,-2),Point(2,-1))],
        [LineSegment(Point(2,2),Point(2,0)), LineSegment(Point(2,4),Point(2,3))],
        [LineSegment(Point(2,0),Point(2,2)), LineSegment(Point(2,3),Point(2,1))],
        [LineSegment(Point(2,2),Point(2,0)), LineSegment(Point(2,-1),Point(2,3))],
        [LineSegment(Point(2,2),Point(2,0)), LineSegment(Point(2,-1),Point(2,0))],
        [LineSegment(Point(2,2),Point(2,0)), LineSegment(Point(2,0),Point(2,-1))],
        [LineSegment(Point(2,0),Point(0,2)), LineSegment(Point(-1,-1),Point(3,3))],
        [LineSegment(Point(2,0),Point(0,2)), LineSegment(Point(3,3),Point(1,1))],
        [LineSegment(Point(2,0),Point(0,2)), LineSegment(Point(2,2),Point(3,3))],
        [LineSegment(Point(2,0),Point(0,2)), LineSegment(Point(4,0),Point(2,-2))],
        [LineSegment(Point(2,0),Point(0,2)), LineSegment(Point(4,0),Point(5,1))]
    ]
    outputs = [
        "none", "none", "none", "infinitely many", "infinitely many",
        "infinitely many", "infinitely many", "infinitely many", Point(2,0),
        Point(2,0), "none", "none", "infinitely many", "infinitely many",
        Point(2,0), Point(2,0), Point(1,1), Point(1,1), "none", "none", "none" ]
    result = []
    for i in range(len(inputs)):
        result.append(inputs[i][0].intersection(inputs[i][1]))
    if result == outputs:  print ("LineSegment.intersection(): Correct")
    else:  print ("LineSegment.intersection(): NOT correct !!")

    # test perp_bisector
    inputs = [
        LineSegment(Point(0,0), Point(2,2)),
        LineSegment(Point(0,2), Point(2,0)),
        LineSegment(Point(2,0), Point(2,2)),
        LineSegment(Point(0,2), Point(2,2)),
        LineSegment(Point(0,0), Point(0,2))
    ]
    outputs = [
        Line((Point(2,0), Point(0,2))),
        Line((Point(0,0), Point(2,2))),
        Line((Point(0,1), Point(1,1))),
        Line((Point(1,0), Point(1,1))),
        Line((Point(0,1), Point(1,1)))
    ]
    result = []
    for i in range(len(inputs)):
        result.append(inputs[i].perp_bisector())
    if result == outputs:  print ("LineSegment.perp_bisector(): Correct")
    else:  print ("LineSegment.perp_bisector(): NOT correct !!")

if __name__ == "__main__":
    test_1()
