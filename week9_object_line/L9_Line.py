import math

class Point(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
        if type(self.x) == float and self.x == int(self.x):
            self.x = int(self.x)
        if type(self.y) == float and self.y == int(self.y):
            self.y = int(self.y)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, p):  # overloads ==
        return self.x == p.x and self.y == p.y

#######################################
class Line(object):
    def __init__(self, param):
        assert type(param) == tuple and len(param) in [2,3]
        # in the form of ax+by+c = 0
        if len(param) == 3:
            a, b, c = param  # unpack
            assert type(a) == type(b) == type(c) == int
            self.__a, self.__b, self.__c = a, b, c
        else:
            p, q = param  # unpack
            assert type(p) == type(q) == Point
            self.__a = q.y-p.y
            self.__b = p.x-q.x
            self.__c = p.y*(q.x-p.x) - p.x*(q.y-p.y)
        assert self.__a != 0 or self.__b != 0

    def getCoeff(self):
        return (self.__a, self.__b, self.__c)

    def __str__(self):
        return str(self.__a) + "x + " + str(self.__b) + "y + " + \
               str(self.__c) + " = 0"

    def sameSlope(self, l):
        try:
            a_s = self.__a / self.__b

        except ZeroDivisionError:
            return l.__b == 0

        try:
            b_s = l.__a / l.__b

        except ZeroDivisionError:
            return False

        return a_s == b_s

    def __eq__(self, line):  # overloads ==
        s = [self.__a, self.__b, self.__c]
        l = [line.__a, line.__b, line.__c]

        if s[1] == 0 or l[1] == 0: #vertical
            return l[1] == 0 and s[1] == 0 and s[2]/s[0] == l[2]/l[0]

        else:
            return s[0]/s[1] == l[0]/l[1] and s[2]/s[1] == l[2]/l[1]


    def contain(self, p):
        return not (self.__a * p.x + self.__b * p.y + self.__c)

    def intersection(self, l):
        if Line.sameSlope(self,l):
            if Line.__eq__(self,l):
                return 'identical'
            return 'parallel'
        ix = (self.__b*l.__c - l.__b*self.__c)/(self.__a*l.__b - l.__a*self.__b)
        iy = (self.__a*l.__c - l.__a*self.__c)/(self.__b*l.__a - l.__b*self.__a)
        return Point(ix,iy)

    def vertical(self):
        return self.__b == 0

def test():
    T, F = True, False
    lines = [
        Line((Point(4,4), Point(-2,-2))),
        Line((Point(-1,-3), Point(3,1))),
        Line((Point(-1,3), Point(4,-2))), Line((Point(-6,8), Point(5,-3))),
        # vertical
        Line((Point(0,-1), Point(0,3))),
        Line((Point(2,-2), Point(2,5))), Line((Point(2,5), Point(2,-3))),
        # horizontal
        Line((Point(-3,0), Point(5,0))),
        Line((Point(-3,2), Point(1,2))), Line((Point(4,2), Point(-3,2)))
    ]
    n = len(lines)

    # test sameSlope
    outputs = [
        T, T, F, F, F, F, F, F, F, F, T, T, F, F, F, F, F, F, F, F,
        F, F, T, T, F, F, F, F, F, F, F, F, T, T, F, F, F, F, F, F,
        F, F, F, F, T, T, T, F, F, F, F, F, F, F, T, T, T, F, F, F,
        F, F, F, F, T, T, T, F, F, F, F, F, F, F, F, F, F, T, T, T,
        F, F, F, F, F, F, F, T, T, T, F, F, F, F, F, F, F, T, T, T ]
    result = []
    for i in range(n):
        for j in range(n):
            result.append(lines[i].sameSlope(lines[j]))
    if result == outputs: print("Line.sameSlope(): Correct")
    else: print("Line.sameSlope(): NOT correct !!")

    # test ==
    outputs = [
        T, F, F, F, F, F, F, F, F, F, F, T, F, F, F, F, F, F, F, F,
        F, F, T, T, F, F, F, F, F, F, F, F, T, T, F, F, F, F, F, F,
        F, F, F, F, T, F, F, F, F, F, F, F, F, F, F, T, T, F, F, F,
        F, F, F, F, F, T, T, F, F, F, F, F, F, F, F, F, F, T, F, F,
        F, F, F, F, F, F, F, F, T, T, F, F, F, F, F, F, F, F, T, T ]
    result = []
    for i in range(n):
        for j in range(n):
            result.append(lines[i] == lines[j])
    if result == outputs:  print("Line.__eq__(): Correct")
    else:  print("Line.__eq__(): NOT correct !!")

    # test contain
    points = [ Point(0,0), Point(0,2), Point(2,2), Point(2,0), Point(1,1) ]
    outputs = [
        T, F, T, F, T, F, F, F, T, F, F, T, F, T, T, F, T, F, T, T, T, T, F, F, F,
        F, F, T, T, F, F, F, T, T, F, T, F, F, T, F, F, T, T, F, F, F, T, T, F, F]
    result = []
    for i in range(n):
        for j in range(len(points)):
            result.append(lines[i].contain(points[j]))
    if result == outputs:  print("Line.contain(): Correct")
    else:  print("Line.contain(): NOT correct !!")

    # test intersection
    outputs = [
        "identical", "parallel", Point(1,1), Point(1,1), Point(0,0), Point(2,2),
        Point(2,2), Point(0,0), Point(2,2), Point(2,2), "parallel", "identical",
        Point(2,0), Point(2,0), Point(0,-2), Point(2,0), Point(2,0), Point(2,0),
        Point(4,2), Point(4,2), Point(1,1), Point(2,0), "identical", "identical",
        Point(0,2), Point(2,0), Point(2,0), Point(2,0), Point(0,2), Point(0,2),
        Point(1,1), Point(2,0), "identical", "identical", Point(0,2), Point(2,0),
        Point(2,0), Point(2,0), Point(0,2), Point(0,2), Point(0,0), Point(0,-2),
        Point(0,2), Point(0,2), "identical", "parallel", "parallel", Point(0,0),
        Point(0,2), Point(0,2), Point(2,2), Point(2,0), Point(2,0), Point(2,0),
        "parallel", "identical", "identical", Point(2,0), Point(2,2), Point(2,2),
        Point(2,2), Point(2,0), Point(2,0), Point(2,0), "parallel", "identical",
        "identical", Point(2,0), Point(2,2), Point(2,2), Point(0,0), Point(2,0),
        Point(2,0), Point(2,0), Point(0,0), Point(2,0), Point(2,0), "identical",
        "parallel", "parallel", Point(2,2), Point(4,2), Point(0,2), Point(0,2),
        Point(0,2), Point(2,2), Point(2,2), "parallel", "identical", "identical",
        Point(2,2), Point(4,2), Point(0,2), Point(0,2), Point(0,2), Point(2,2),
        Point(2,2), "parallel", "identical", "identical"
    ]
    result = []
    for i in range(n):
        for j in range(n):
            result.append(lines[i].intersection(lines[j]))
    if result == outputs:  print ("Line.intersection(): Correct")
    else:  print ("Line.intersection(): NOT correct !!")

test()
