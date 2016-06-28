class Node:
	def __init__(self):
		self.value = 0
		self.next = None
	

class LinkedList:
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
			while current != None:
				print current.value,"-->",
				current = current.next
			print None
		else:	
			print "Empty Linked list"
		
	def removeDuplicates(self):
		current = self.head
		if current is not None:
			fast = current.next
			while current != None and fast != None:
				if current.value == fast.value:
					current.next = fast.next	
					fast = fast.next
				else:
					current = current.next
					fast = fast.next
		else:
			return "Empty Linked List"

if __name__ == "__main__":
	llist = LinkedList()
	print "Menu : "
	print "1 - append list"
	print "2- print list"
	print "3 - remove duplicates from sorted list"
	n = raw_input("Choose 1/2/3 : ")
	while True:
		if n == '1':
			value = input("Enter any value of node : ")
			llist.append(value)
		elif n == '2':
			llist.printList()
		elif n == '3':
			llist.removeDuplicates()
		else:
			print "Invalid option choosen.Try again..."
			break
		n = raw_input("Choose 1/2/3 : ")

