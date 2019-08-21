from random import *
from time import *

def open():
  print("******************************")
  print("*      즐거운 수학 시간       *")
  print("*                            *")
  print("******************************")

  print("1. Addition")
  print("2. Difference")
  print()

  num=int(input("Select: "))
  return num

def add():
	print("******************************")
	print("*      즐거운 더하기 시간     *")
	print("*                            *")
	print("******************************")

	numLevel=int(input("숫자의 자릿수: "))
	print()
	stop = False
	pts=[0]
	
	def loop(lev: int, counter: int, pts):
		global stop
		num1=randint(1, 10**lev)
		num2=randint(1, 10**lev)
		t=time()
		ans=input("#{}. {}+{}=".format(counter, num1, num2))
		ans=int(ans)
		t2=time()
		if ans==num1+num2:
			pass
			pts[0]+=1
		elif ans==0:
			stop=True
			return 0
		else:
			print("병신새끼야")
			print("답: {}".format(num1+num2))
			pts[0]-=10
			
		dt=str(t2-t-0.4)
		print("| {}초 | {}점".format(dt[:5], pts[0]))
		print("----------------------------")
		print()
	
	counter=1
	while not stop:
		a=loop(numLevel, counter, pts)
		counter+=1
		if a==0:
			break
	
  
def main():
	while 1:
		num=open()
		
		if num==1:
			print()
			add()
			
		if num==2:
			pass
		
main()