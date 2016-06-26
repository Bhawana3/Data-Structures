def is_maching_pair(a,b):
	if a == '{' and b == '}':
		return True
	elif a == '[' and b == ']':
		return True
	elif a == '(' and b == ')':
		return True
	else:
		return False
class Node:
	def __init__(self):
		self.value = '' 
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

	""" Given a string check order of opening and closing bracket"""
	def check_brackets(self,string):
		i = 0
		while i < len(string):
			if string[i] == '{' or string[i] == '[' or string[i] == '(':
				self.push(string[i])
			elif string[i] == '}' or string[i] == ']' or string[i] == ')':
				if self.top is not None:
					opening = self.pop()
					match = is_maching_pair(opening,string[i])
					if match == False:
						return "brackets are not in sequence"
						break
					else:
						pass	
				else:
					return False
			else:
				pass
			i += 1
		if self.top is None:			# checks if the stack is empty or not
			print "sequence is correct"	# if stack is empty that means there are equal number of brackets are present
			return True
		else:
			return False			

if __name__ == '__main__':
	stack = Stack()
	char_stack = Stack()
	print "Menu : "
	print "1 - push new node into stack "
	print "2 - print stack"
	print "3 - delete node from given stack"
	print "4 - check sequence is in order or not"
	print "5 - print character stack"
	n = raw_input('Choose any number 1/2/3/4/5 : ')
	while True:
		if n == '1':
			value = raw_input("Enter any string value of node: ")
			stack.push(value)
		elif n == '2':
			stack.print_stack()
		elif n == '3':
			print stack.pop()
		elif n == '4':
			string = raw_input("Enter any string containing brackets : ")
			print char_stack.check_brackets(string)
		elif n == '5':
			char_stack.print_stack()
		else:
			print "Invalid option. Exiting..."
			break
		n = raw_input('Choose any number 1/2/3/4/5 : ')

