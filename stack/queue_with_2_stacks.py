class Node:
	def __init__(self):
		self.value = value
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
	
	def printStack(self):
		current = self.top	
		if current is not None:
			while current != None:
				print current.value,"-->",
				current = current.next
			print None
		else:
			print "empty stack"

class queue_with_2_stacks:
	""" Initializing 2 stack class"""	
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	""" push element into first stack"""	
	def enqueue(self,value):
		self.s1.push(value)
	
	def dequeue(self):
		current = self.s1.top
		if current is not None:
			while current != None:
				self.s2.push(self.s1.pop())	# pop node from first stack and push it into second stack
				current = current.next
			return self.s2.pop()			# pop node from second stack
		else:
			return "Empty Queue"

	def printQueue(self):
		return self.s1.printStack()
		
if __name__ == "__main__":
	queue = queue_with_2_stacks()
	print "Menu : "
	print "1 - enqueue node into queue"
	print "2 - dequeue queue"
	print "3 - print queue"
	n = raw_input("Enter value 1/2/3 : ")
	while True:
		if n == '1':
			value = input("Enter value to insert into queue : ")
			queue.enqueue(value)
		elif n == '2':
			print queue.dequeue()
		elif n == '3':
			queue.printQueue()
		else:
			print "Invalid option choosen. Exiting...."
			break
		n = raw_input("Enter value 1/2/3 : ")

			
