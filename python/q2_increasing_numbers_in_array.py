''' Problem Statement :

1) Given an array of numbers, return whether the array has three numbers that
 are increasing, that is index i,j,k such that i<j<k and a[i]<a[j]<a[k].

Example:
	Given: [4,2,5,1,7]
	Output: True

'''

import unittest

def increasing_order(array):

	if len(array) < 3:
		raise ValueError('Number of elements in array are less than 3')

	
if __name__ == '__main__':
	unittest.main()



