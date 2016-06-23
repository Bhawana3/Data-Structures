class Node:
	def __init__(self):
		self.value = 0	
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.head = None
	
	""" insert node into circular LL"""
	def circular_linked_list(self,value):
		temp = Node()
		temp.value = value
		current = self.head
		if current is not None:
			while current.next != self.head:
				current = current.next
			current.next = temp
			temp.next = self.head
		else:
			temp.next = temp
		self.head = temp

	""" Find loop in a linked list"""
	def find_loop(self):	
		fast = self.head
		slow = self.head
		if self.head is not None:
			while fast != None and fast.next.next != None:
				if slow != fast:	# when slow becomes equal to fast then there must be a loop
					slow = slow.next
					fast = fast.next.next
				else:
					return True
			return False 
		else:
			return "Empty Linked List"

class Linkedlist:
	def __init__(self):
		self.head = None

	def append(self,value):
		temp = Node()	
		temp.value = value
		current = self.head	
		if current is not None:
			while current.next != None:
				current = current.next
			current.next = temp
		else:
			self.head = temp
		
	def printList(self):
		current = self.head
		if current is not None:
			while current is not None:
				print current.value,'-->',
				current = current.next
			print None
		else:
			print "No linked list exists"

	""" Find loop in a linked list"""	
	def find_loop(self):
		slow = self.head	
		fast = self.head
		if self.head is not None:
			while fast != None and fast.next != None:
				slow = slow.next
				fast = fast.next.next
				if slow == fast:	# when slow becomes equal to fast then there must be a loop
					return True
				return False
		else:
			return "Empty Linked List"
# program starts from here
if __name__ == "__main__":
	Llist = Linkedlist()
	circularLL = CircularLinkedList()
	print "Menu : "
	print "1 - append node in linked list"
	print "2 - print linked list"
	print "3 - find loop in linked list"
	print "4 - insert node into circular LL"
	print "5 - find loop in circular LL"
	n = raw_input("Choose 1/2/3/4/5 : ")
	while True:
		if n == '1':
			value = input("Enter any value of node: ")
			Llist.append(value)
		elif n == '2':
			Llist.printList()
		elif n == '3':
			print Llist.find_loop()
		elif n == '4':
			value = input("Choose any value to append : ")
			circularLL.circular_linked_list(value)
		elif n == '5':
			print circularLL.find_loop()
		else:
			print "Invalid option choosen. Exiting..."
			break
		
		n = raw_input("Choose 1/2/3/4/5 : ")
