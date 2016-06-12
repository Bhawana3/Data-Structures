class Node():
	def __init__(self,value):
		self.value = value
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = Node(2)
	def append(self,value):
		temp = Node(value)		# node to be appended
		current = self.head
		if self.head:
			while current.next != None:
				current = current.next
			current.next = temp
		else:
			current.next = None
	def traverse(self):
		counter = 1
		current = self.head
		if self.head:
			while current.next != None:
				current = current.next
				counter += 1
			return counter
		else:
			return 1
	def get_position(self,position):
		current = self.head
		counter = 1 
		if position >= 1:
			while self.head :
				if counter == position:
					return current.value
				counter += 1
				current = current.next
		else:
			return 0
				

l1 = LinkedList()
print l1.head.value
#print l1.head.next

print l1.traverse()
l1.append(10)
print l1.traverse()
l1.append(50)
print l1.traverse()
l1.append(3)
print l1.traverse()

print l1.get_position(4)
print l1.get_position(1)
print l1.get_position(2)
print l1.get_position(3)
