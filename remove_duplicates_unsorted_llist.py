class Node:
	def __init__(self):
		self.value = value
		self.next = None

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
			while current != None:
				print current.value ,"-->",
				current = current.next
			print None
		else:
			print "Empty Linked List"

	""" Remove duplicates from unsorted linked list"""
	""" Traverse through linked list and compare each node value
		with another node value"""
	
	def removeDuplicates(self):
		ptr1 = self.head
		dup = None
		if self.head is not None:
			while ptr1 != None and ptr1.next != None:
				ptr2 = ptr1				# both starts from same position
				while ptr2 != None and ptr2.next != None:
					if ptr1.value == ptr2.next.value:
						dup = ptr2.next
						ptr2.next = ptr2.next.next
					ptr2 = ptr2.next
				ptr1 = ptr1.next
		else:
			return "Empty linked list"

if __name__ == "__main__":
	llist = Linkedlist()
	print "Menu : "
	print "1 - append list"
	print "2 - print list"
	print "3 - remove duplicates from the list"
	n = raw_input("Choose 1/2/3 : ")
	while True:
		if n == '1' :
			value = input("Enter any value of node : ")
			llist.append(value)
		elif n == '2':
			llist.printList()
		elif n == '3':
			llist.removeDuplicates()
		else:
			print "Invalid option choosen.Exiting..."
			break
		n = raw_input("Choose 1/2/3 : ")
