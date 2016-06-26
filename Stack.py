class Node:
	def __init__(self):
		self.value = 0 
		self.next = None

class Stack:
	def __init__(self):
		self.top = None

	""" push new node into stack"""
	def push(self,value):
		current = self.top
		temp = Node()
		temp.value = value
		if current is not None:
			temp.next = current
			self.top = temp
		else:
			self.top = temp
	
	""" print stack"""
	def print_stack(self):
		current = self.top
		while current is not None:
			print current.value,'-->'
			current = current.next
		print None

	""" Pop node from stack"""
	def pop(self):
		current = self.top
		if current is not None:
			temp = current.next
			self.top = temp
			current.next = None
			return current.value
		else:
			return "No stack exists"	


if __name__ == '__main__':
	stack = Stack()
	print "Menu : "
	print "1 - push new node into stack "
	print "2 - print stack"
	print "3 - delete node from given stack"
	n = raw_input('Choose any number 1/2/3 : ')
	while True:
		if n == '1':
			value = input("Enter any value of node: ")
			stack.push(value)
		elif n == '2':
			stack.print_stack()
		elif n == '3':
			print stack.pop()
		else:
			print "Invalid option. Exiting..."
			break
		n = raw_input('Choose any number 1/2/3 : ')
