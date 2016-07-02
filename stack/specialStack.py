""" Make a special stack class which has same push,pop methods 
	plus one additional method to show minimum value of stack
	 in Time complexity of O(n)"""


class Node:
	def __init__(self):
		self.value = 0
		self.next = None

class Stack:
	def __init__(self):
		self.top = None
		
	def push(self,value):
		temp = Node()
		temp.value = value
		current = self.top
		if current is not None:
			temp.next = current
			self.top = temp
		else:
			self.top = temp
		
	def pop(self):
		current = self.top	
		if current is not None:
			temp = current.next
			self.top = temp
			current.next = None
			return current.value
		else:
			return "underflow"
	
	def printStack(self):
		current = self.top
		if self.top is not None:
			while current != None:
				print current.value,"-->",
				current = current.next
			print None
		else:
			print "Empty Stack"
		
class SpecialStack:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()	

	def insert_node(self,value):
		if self.stack2.top is not None and self.stack1.top is not None:
			print self.stack2.top.value
			if self.stack2.top.value > value:
				self.stack2.push(value)
				self.stack1.push(value)
			else:
				self.stack1.push(value)
				print self.stack1.top.value
		else:
			self.stack1.push(value)
			self.stack2.push(value)

	def pop_node(self):
		if self.stack1.top is not None and self.stack2.top is not None:
			if self.stack2.top.value == self.stack1.top.value:
				self.stack1.pop()
				self.stack2.pop()
			else:
				self.stack1.pop()
		else:	
			print "Empty stack"

	def print_stack(self):
		self.stack1.printStack()
		self.stack2.printStack()
	
	def getMin(self):
		if self.stack2.top is not None:
			return self.stack2.top.value
		else:
			return "Empty Stack"

if __name__ == "__main__":
	specialStack = SpecialStack()
	print "Menu : "
	print "1 - push node into special stack"
	print "2 - pop node from special stack"
	print "3 - print stack"
	print "4 - get minimum value in stack"
	n = raw_input("Choose 1/2/3/4 : ")
	while True:
		if n == '1':
			value = input("Enter value to push into stack : ")
			specialStack.insert_node(value)	
		elif n == '2':
			print specialStack.pop_node()
		elif n == '3':
			specialStack.print_stack()
		elif n == '4':
			print specialStack.getMin()
		else:
			print "Invalid option choosen. Exiting..."
			break
		n = raw_input("Choose 1/2/3/4 : ")
