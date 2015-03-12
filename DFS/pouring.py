import copy
import itertools


class Bottles(object):
	
	def __init__(self):

		self.max_ten = 10
		self.max_seven = 7
		self.max_four = 4

		self.ten = 0
		self.seven = 7
		self.four = 4

	def pour(self,source,target):
		
		s = getattr(self,source)
		t = getattr(self,target)

		if (s == 0):
			return
		
		if (target == "ten" and t == 10) or \
		   (target == "seven" and t == 7) or\
		   (target == "four" and t ==4):
			return

		if s+t > getattr(self,"max_"+target):
			setattr(self,source,s + t - getattr(self,"max_"+target))
			setattr(self,target,getattr(self,"max_"+target))
			return 

		else:
			setattr(self,source,0)
			setattr(self,target,s+t)
			return

def depth_first_search(bottles):

	#print(bottles.ten,bottles.seven,bottles.four)
	if (bottles.ten,bottles.seven,bottles.four) in visited:
		return False

	visited.append((bottles.ten,bottles.seven,bottles.four))
	if (bottles.seven == 2) or (bottles.four == 2):
		print ("TRUE!!")
		return True

	for s,t in itertools.product(["ten","seven","four"],repeat=2):
		if s == t:
			continue
		b = copy.copy(bottles)
		b.pour(s,t)
		if depth_first_search(b):
			print("--->",b.ten,b.seven,b.four)
			return True


if __name__ == "__main__":

	bottles = Bottles()
	visited = []
	depth_first_search(bottles)

