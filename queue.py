class Node:
	def __init__(self):
		self.value = 0
		self.next = None

class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
		self.length = 0

	""" add node from rear end into queue"""
	def enqueue(self,value):
		temp = Node()
		temp.value = value
		rear = self.rear
		if self.front is not None and rear is not None:
			rear.next = temp
			self.rear = temp
		else:
			self.rear = temp
			self.front = self.rear 
		self.length += 1

	""" delete node from front"""
	def dequeue(self):
		front = self.front
		if front is not None:
			temp = front.next
			self.front = temp
			front.next = None
			self.length -= 1
			return front.value
		else:
			"Empty queue"

	""" return front without removing it"""
	def peek(self):
		if self.front is not None:
			return self.front.value
		else:
			return "Empty Queue"	
	
	def printQueue(self):
		front = self.front
		rear  = self.rear
		if self.front is not None:
			while front != None:
				print front.value,'-->',
				front = front.next
			print None
		else:
			print "empty queue"
		print "size of queue is ",self.length

if __name__ == "__main__" :
	queue = Queue()
	print "Menu : "
	print "1 - insert node(enqueue)"
	print "2 - delete node(dequeue)"
	print "3 - print queue"
	print "4 - to know the front element"
	n = raw_input("Choose 1/2/3/4 : ")
	while True:
		if n == '1':
			value = input("Enter any node value : ")
			queue.enqueue(value)
		elif n == '2':
			print queue.dequeue()
		elif n == '3':
			queue.printQueue()
		elif n == '4':
			print queue.peek()
		else:
			print "Invalid option choosen. Exiting..."
			break
		
		n = raw_input("Choose 1/2/3/4 : ")
