import unittest

def generate_parenthesis(n):
	if n < 1:
		raise ValueError("Value of n cannot be less than 1")

	return generate_parenthesis_helper('',n,n,[])

def generate_parenthesis_helper(p,left,right,parens):
	if left:
		generate_parenthesis_helper(p + '(', left-1, right,parens)
	if right > left:
		generate_parenthesis_helper(p + ')', left, right-1,parens)
	
	if not right:
		parens += p,    # that comma at the end appends to list without spling the string
	return parens

class Test(unittest.TestCase):
	def setUp(self):
		self.expected = ['()()()','()(())','(())()','(()())','((()))']
		self.n = 3

	def test_generate_parenthesis(self):
		actual = generate_parenthesis(self.n)
		self.assertEqual(sorted(actual),sorted(self.expected))


	def test_generate_parenthesis_helper(self):
		actual = generate_parenthesis_helper('',self.n,self.n,[])
		self.assertEqual(sorted(actual),sorted(self.expected))

if __name__ == '__main__':
	unittest.main()