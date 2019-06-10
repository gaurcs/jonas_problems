# Problem Statement: Write a queue that can use push, pop, peek using only stacks. The stacks have the same functions push, pop, or peek.
# Queue - A FIFO data structure. 
# Stack - A LIFO data structure.
#
import unittest
class Queue(object):
     
    def __init__(self):
        self.stack_1 = [] #using list as a stack
        self.stack_2 = []
 
    def push(self, value):
        self.stack_1.append(value)
 
    def pop(self):
        if not self.stack_1 and not self.stack_2:
            raise IndexError("pop on empty queue")
 
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
 
        return self.stack_2.pop()


class Test(unittest.TestCase):

	def test_push(self):
		q = Queue()
		q.push(8)
		q.push(9)
		q.push(11)
		q.push(13)
		self.assertEqual(q.stack_1, [8,9,11,13])

	def test_pop(self):
		q = Queue()
		q.push(8)
		q.push(9)
		q.push(11)
		q.push(13)
		self.assertEqual(q.pop(),8)
		self.assertEqual(q.stack_1,[])
		self.assertEqual(q.stack_2,[13,11,9])
		self.assertEqual(q.pop(),9)

	def test_jon(self):
		q = Queue()
		q.push(1)
		q.push(2)
		q.push(3)
		self.assertEqual(q.pop(),1)
		q.push(4)
		q.push(5)
		self.assertEqual(q.pop(),2)
		q.push(6)
		self.assertEqual(q.pop(),3)
		self.assertEqual(q.pop(),4)
		self.assertEqual(q.pop(),5)
		self.assertEqual(q.pop(),6)

if __name__ == '__main__':
	unittest.main()


