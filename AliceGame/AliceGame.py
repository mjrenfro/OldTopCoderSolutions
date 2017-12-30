#Recursive solution to the AliceGame problem 
#Created by TopCoder

#Algorithm design is taken from Advanced Programming and Algorithms 
#slide show by the University of Tennessee 
#Link : http://web.eecs.utk.edu/courses/spring2016/cosc494/notes/Alice/AliceGame.pdf

import math

import unittest

class AliceGame:

	#Wrapper function to be compatible with the function signature
	#TopCoder expects.
	def findMinimumValue(self, x,y):
		return self.solver(x,y,-1)


	def solver(self, x, y, r):

		#Determine the number of turns this game had
		#(if this is the first call)
		if r is -1:
			r=math.sqrt(x+y)

 		#----------BASE CASE---------#

 		#1. Not valid if the root is not an integer
		if not r.is_integer(): return -1

		#2. 2 is not a valid score
		if x is 2 or y is 2: return -1

		#3. 0 score means 0 turns
		if x is 0: return 0

		#a <= 2r
		if x <= 2*r:

			#a is odd
			if x %2 ==1: return 1

			#a is even
			else: return 2

		# a = 2r +1
		if x == 2*r +1 : return 3

		#-----------RECURSIVE CALL-----------#

		#Change parameters and make recursive call
		x-=(2*r-1)
		r-=1

		return self.solver(x,y,r)+1

#Testing against the examples provided by TopCoder
class TestStringMethods(unittest.TestCase):
	def setUp(self):
		self.aliceGame = AliceGame()

	def test_return_two(self):
		self.assertEqual(self.aliceGame.findMinimumValue(8,17),2)

	def test_return_three(self):
		self.assertEqual(self.aliceGame.findMinimumValue(17,8),3)

	def test_return_zero(self):
		self.assertEqual(self.aliceGame.findMinimumValue(0,0),0)

	def test_invalid(self):
		self.assertEqual(self.aliceGame.findMinimumValue(9,9),-1)

	def test_large_score(self):
		self.assertEqual(self.aliceGame.findMinimumValue(500000,500000), 294)


if __name__ == '__main__':
    unittest.main()






