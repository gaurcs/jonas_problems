''' Problem Statement :

1) Given an array of numbers, return whether the array has three numbers that
 are increasing, that is index i,j,k such that i<j<k and a[i]<a[j]<a[k].

Example:
	Given: [4,2,5,1,7]
	Output: True

'''

import unittest

def increasing_order(array):

	# if 'Number of elements in array are less than 3'
	if len(array) < 3:
		return False

	# first two pointers to max value
	first = float('inf')
	second = float('inf')
	for i in range(0,len(array)):
		if array[i] <= first:
			first = array[i]
		elif array[i] <= second:
			second = array[i]
		else:
			return True

	return False

class Test(unittest.TestCase):
	data = [
	([], False),
	([1,1], False),
	([1,1,1], False),
	([1,2,3,4,5,6], True),
	([6,5,4,3,2,1], False),
	([6,5,4,3,2,1,0,2,4], True),
	([1,2,1], False),
	([6,7,4,5,2,3,1], False),
	([6,7,4,5,2,3,1,4], True)]

	def test_increasing_order(self):
		for [test_list, expected] in self.data:
			actual = increasing_order(test_list)
			self.assertEqual(actual, expected)


if __name__ == '__main__':
	unittest.main()



