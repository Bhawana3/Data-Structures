class Queue:
	""" initializing empty list named queue"""
	def __init__(self):
		self.queue = []

	""" append new node into queue(list)"""
	def enqueue(self,new_node):
		self.queue.append(new_node)

	""" pop first element from the queue"""
	def dequeue(self):
		if self.queue != []:
			return self.queue.pop(0)
		else:
			return "Empty queue - underflow"
	
	""" return first element from the queue"""
	def peek(self):
		if self.queue != []:
			return self.queue[0]
		else:
			return "Empty queue"

	def printQueue(self):
		for node in self.queue:
			print node,'-->',
		print None	

if __name__ == "__main__":
	queue = Queue()
	print "Menu : "
	print "1 - appending new element in the queue"
	print "2 - dequeuing queue"
	print "3 - show first element in the queue"
	print "4 - print queue"
	n = raw_input("Enter any number 1/2/3/4 : ")
	while True:
		if n == '1':
			value = input("Enter value of new element : ")
			queue.enqueue(value)
		elif n == '2':
			print queue.dequeue()
		elif n == '3':
			print queue.peek()
		elif n == '4':
			queue.printQueue()
		else:
			print "Invalid option choosen.Exiting..."
			break
		n = raw_input("Enter any number 1/2/3/4 : ")
		

