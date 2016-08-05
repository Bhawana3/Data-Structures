class Node:
	def __init__(self):
		self.value = 0
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# delete middle node 	
	def deleteMid(self):
		if self.head is None:
			return Node
		elif self.head.next == None:
			self.head = None
		else:
			slow = self.head
			fast = self.head
			prev = None					# prev keeps track of slow's previous node
			while fast != None and fast.next != None:
				fast = fast.next.next
				prev = slow
				slow = slow.next
			prev.next = slow.next
			slow.next = None
	
	def printList(self):
		current = self.head
		if current is not None:
			while current != None:
				print current.value, "-->",
				current = current.next
			print None
		else:
			print "Empty Linked list"

	def appendList(self,new_val):
		temp = Node()
		temp.value = new_val
		current = self.head
		if current is None:
			self.head = temp
		else:
			while current.next != None:
				current = current.next
			current.next = temp

if __name__ == "__main__":
	LList = LinkedList()
	print "1 - append node into list"
	print "2 - print list"
	print "3 - delete middle node in list"
	n = raw_input("Choose from above options: ")
	while True:
		if n == '1':
			value = input("Enter any value of node: ")
			LList.appendList(value)
		elif n == '2':
			LList.printList()
		elif n == '3':
			LList.deleteMid()
		else:
			print "Exiting.."
			break
		n = raw_input("Choose from above options: ")
			
		
		

