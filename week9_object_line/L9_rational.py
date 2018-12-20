def gcd(a, b):
  b, a = sorted([a,b])
  def inner(p, q):
    return inner(q, p%q) if q else p
  return inner(a,b)

class RationalNum:
  def __init__(self, numer, denom=1):
    self._numer = numer
    self._denom = denom

  def reduce(self):
    g = gcd(self._numer, self._denom)
    new_numer = self._numer // g
    new_denom = self._denom // g
    new_rational = RationalNum(new_numer, new_denom)
    return new_rational

  def __add__(self, rational):
    new_denom = self._denom * rational._denom
    new_numer = self._numer * rational._denom + self._denom * rational._numer
    new_rational = RationalNum(new_numer, new_denom)
    new_rational.reduce()
    return new_rational

  def __sub__(self, rational):
    new_denom = self._denom * rational._denom
    new_numer = self._numer * rational._denom - self._denom * rational._numer
    new_rational = RationalNum(new_numer, new_denom)
    new_rational.reduce()
    return new_rational

  def __mul__(self, rational):
    new_denom = self._denom * rational._denom
    new_numer = self._numer * rational._numer
    new_rational = RationalNum(new_numer, new_denom)
    new_rational.reduce()
    return new_rational

  def __eq__(self, rational):

    return (self.reduce()._denom, self.reduce()._numer) \
        == (rational.reduce()._denom, rational.reduce()._numer)

  def __str__(self):
    return "{}/{}".format(self._numer, self._denom)

a = RationalNum(4, 5)
b = RationalNum(8, 10)
