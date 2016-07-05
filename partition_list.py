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
	
	""" Insert node into front of list"""
	def insert_into_front(self,value):
		temp = Node()
		temp.value = value
		current = self.head
		if current is not None:
			temp.next = current
			self.head = temp
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
			print "Empty Linked list"
	
	""" partition linked list from the given value into smaller
	 in left side and larger in right side of the element"""

	def partition(self,value):
		smaller_list = LinkedList()
		larger_list = LinkedList()
		current = self.head
		if current is not None:
			while current != None:
				if current.value < value:
					smaller_list.append(current.value)
				elif current.value == value:
					larger_list.insert_into_front(current.value)
				else:
					larger_list.append(current.value)
				current = current.next
			small = smaller_list.head		
			if small is not None:
				while small.next != None:
					small = small.next
				small.next = larger_list.head		# merge smaller list with larger list
			else:
				smaller_list.head = larger_list.head	# head pointer of smaller list pointing towards none
			smaller_list.printList()			
		else:
			print "Empty linked list"

if __name__ == "__main__":
	Llist = LinkedList()
	print "Menu :"
	print "1 - append into list"
	print "2 - insert into front of list"
	print "3 - print list"
	print "4 - partition list"
	n = raw_input("Choose from above option : ")
	while True:
		if n == '1':
			value = input("Enter value to node : ")
			Llist.append(value)
		elif n == '2':
			value = input("Enter value to node : ")
			Llist.insert_into_front(value)
		elif n == '3':
			Llist.printList()
		elif n == '4':
			value = input("Enter value to find in the list : ")
			Llist.partition(value)
		else:
			print "Invalid option choosen.Exiting.."
			break
		n = raw_input("Choose from above option : ")

