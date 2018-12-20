class LinearEq(object):
  def __init__(self, m, b):
    self._m = m; self._b = b;

  def __str__(self):
    if self._m == 0:
      if self._b == 0:
        return "y=0"
      return "y={}".format(self._b)

    if self._b == 0:
      return "y={}x".format(self._m)

    return "y={0}x+{1}".format(self._m, self._b)

  def value(self, x):
    return self._m * x + self._b

  def compose(self, eq_):
    ret = LinearEq(self._m * eq_._m, self._m * eq_._b + self._b)
    return ret

  def __add__(self, eq_):
    ret = LinearEq(self._m + eq_._m, self._b + eq_._b)
    return ret

class Clock(object):
  def __init__(self, h=0, m=0):
    try:
      assert isinstance(h, int)
      assert isinstance(h, int)
      self._h = h; self._m = m;
    except:
      self._h = 0; self._m = 0;

    self._h += self._m // 60;
    self._m %= 60

  def __add__(self, clock):
    assert type(clock) == int or type(clock) == Clock
    new_h = self._h; new_m = self._m
    if isinstance(clock, int):
      new_h += clock
    else:
      new_h += clock._h; new_m += clock._m;

    ret = Clock(new_h, new_m)
    return ret

  def __radd__(self, clock):
    return self.__add__(clock)

  def __str__(self):
    return "{} hours, {} minutes".format(self._h, self._m)

def test1():
  print(LinearEq(0,0))
  print(LinearEq(-2,0))
  print(LinearEq(3,-4))
  print(LinearEq(5,5))
  a = LinearEq(2,3)
  print(a)
  b = LinearEq(3,4)
  print(b)
  print(a.value(3) + b.value(2))
  c = a.compose(b)
  d = a+b
  print(c)
  print(d)
  print(c.value(3) + d.value(3))
def test2():
  inst1_clock = Clock(10,35)
  inst2_clock = Clock(5,25)
  inst3_clock = Clock()
  inst4_clock = Clock('a')
  print(inst1_clock)
  print(inst3_clock)
  print(inst4_clock)
  sum1_clock = inst1_clock + inst2_clock
  print(sum1_clock)
  sum2_clock = inst2_clock + 4
  print(sum2_clock)
  sum3_clock = 4 + inst2_clock
  print(sum3_clock)

def main():
  test1()
  print
  test2()

main()
