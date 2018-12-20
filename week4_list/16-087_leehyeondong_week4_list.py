#=================================================
#  Homework : List and Tuple
#  ID   : 16-087
#  NAME : Lee Hyeondong
#=================================================
# For P1 ~P4 Medals
#=================================================
from typing import *

countries = ['Australia', 'Austria', 'Belarus', 'Belgium', 'Canada', 'China', 'Czech Republic', \
'Finland', 'France', 'Germany', 'Great Britain', 'Hungary', 'Italy', 'Japan', 'Kazakhstan', \
'Latvia', 'Liechtenstein', 'Netherlands', 'New Zealand', 'Norway', 'OAR', 'Poland', \
'Republic of Korea', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United States']

gold = [0, 5, 2, 0, 11, 1, 2, 1, 5, 14, 1, 1, 3, 4, 0, 0, 0, 8, 0, 14, 2, 1, 5, 1, 0, 0, 7, 5, 1, 9]

silver = [2, 3, 1, 1, 8, 6, 2, 1, 4, 10, 0, 0, 2, 5, 0, 0, 0, 6, 0, 14, 6, 0, 8, 2, 1, 0, 6, 6, 0, 8]

bronze = [1, 6, 0, 0, 10, 2, 3, 4, 6, 7, 4, 0, 5, 4, 1, 1, 1, 6, 2, 11, 9, 1, 4, 0, 1, 2, 1, 4, 0, 6]

#=================================================
#  P1_MakeTotalMedal()
#=================================================

def P1_MakeTotalMedal() -> List[Tuple]:
  """
  pair_list = []
  CountryTuple = lambda i: (gold[i] + silver[i] + bronze[i], countries[i])
  for i in range(len(countries)):
    pair_list.append(CountryTuple(i))

  return pair_list
  """

  return list(map(lambda i: (gold[i] + silver[i] + bronze[i], countries[i]), range(len(countries))))

print("#1")
print(P1_MakeTotalMedal())
print()


#=================================================
#  P2_PrintTopFive ()
#=================================================

def P2_PrintTopSeven() -> None:
  Compare = lambda count1: (gold[count1], silver[count1], bronze[count1])
  PrintInfo = lambda count: print("{:22s} {:2d} {:2d} {:2d}".format(countries[count], gold[count], silver[count], bronze[count]))
  country = sorted(list(range(len(countries))), key = Compare, reverse = True)
  for i in country[:7]:
    PrintInfo(i)

print("#2")
P2_PrintTopSeven()
print()

#=================================================
#  P3_OnlyOneKind ()
#=================================================
def P3_OnlyOneKind() -> List[str]:
  return list(map(lambda i: countries[i], list(filter(lambda i: (gold[i], silver[i], bronze[i]).count(0) == 2, list(range(len(countries)))))))

print("#3")
print(P3_OnlyOneKind())
print()

#=================================================
#  P4_PrintHistogram()
#=================================================
interval_length = 4
def P4_PrintHistogram():
  global interval_length
  total_medal_list = list(map(lambda i: (gold[i] + silver[i] + bronze[i]) // interval_length, range(len(countries))))
  for i in range(max(total_medal_list) + 1):
    print("{:7s} {:12s}".format(str(interval_length * i)+ '~'+ str(interval_length * (i+1) - 1)+':', '*' * total_medal_list.count(i)))

print("#4")
P4_PrintHistogram()
print()

#=================================================
#  P5_ReverseSlicedList ( )
#=================================================
def P5_ReverseSlicedList(alist) -> List:
  return list(map(lambda i: alist[i:], list(range(len(alist)-1, -1, -1))))

print("#5")
a = ['a','b','c','d','e','f']
print(P5_ReverseSlicedList(a))
b = ['a','b','c',1,2,3]
print(P5_ReverseSlicedList(b))
print()

#=================================================
#  P6_TransposeMatrix( )
#=================================================
def P6_TransposeMatrix(matrix) -> List:
  return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("#6")
M1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print (P6_TransposeMatrix(M1))  #[[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
M2 = [[1,2,3],[4,5,6] ]
print (P6_TransposeMatrix(M2))
print()

#=================================================
#  P7_ZeroSum ( )
#=================================================
def P7_ZeroSum(L) -> List:
  list = []
  for i in range(len(L)-2):
    for j in range(i+1, len(L)-1):
      if -(L[i] + L[j]) in L[j+1:]:
        list.append((L[i], L[j], -(L[i] + L[j])))

  return list

print("#7")
L1 = [1,2,-3,4,5,-1]
print(P7_ZeroSum(L1))  #[(1, 2, -3), (-3, 4, -1)]
L2 = [1,2,3,4,5]
print(P7_ZeroSum(L2))
print()

#=================================================
#  P8_PowerSet ( )
#=================================================

def P8_PowerSet(n):
  set_ = list(range(1, n+1))
  subsets = [[]]
  for element in set_:
    for ind in range(len(subsets)):
      subsets.append(subsets[ind] + [element])
  return subsets

print("#8")
print(P8_PowerSet(3))
print()

#=================================================
#  P9_SortLists ( ):
#=================================================
def P9_SortLists (a):
  def sumFunc(list):
    return sum(list)

  a.sort(key = sumFunc, reverse = True)
  return a

print("#9")
a = [[5,11], [1,5,3], [20], [1,2,3,4,5], [2,4,8]]
print(P9_SortLists (a))
print()

#=================================================
#  P10_SieveOfEratosthenes( )
#=================================================

def P10_SieveOfEratosthenes(n):
  composite_list = []; prime_list = []
  for i in range(2, n+1):
    if i not in composite_list:
      prime_list.append(i); composite_list.append(i)
      for j in range(i*i, n+1, i):
        composite_list.append(j)

  return prime_list

print("#10")
print(P10_SieveOfEratosthenes(30))
print()

#=================================================
#  P11_OccurrencesOfIntegers( )
#=================================================

def P11_OccurrencesOfIntegers(integers):
  numArr = []
  integers.sort()
  i = 0

  while i <= len(integers)-1:
    numArr.append([integers[i], integers.count(integers[i])])
    i += integers.count(integers[i])

  return numArr

print("#11")
arr = [ 3,7,33,4,5,3,4,7,8,23,23,23,8,3,5]
print(P11_OccurrencesOfIntegers(arr))
print()
