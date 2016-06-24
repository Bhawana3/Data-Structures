class Node:
	def __init__(self):
		self.value = value
		self.head = None

class Linkedlist:
	def __init__(self):
		self.head = None
	
	""" Insert node in sorted manner(ascending)"""	
	def insert_in_sorted_list(self,value):
		temp = Node()
		temp.value = value
		if self.head is None:			# when linked list is empty
			self.head = temp
			temp.next = None
		elif self.head.value > temp.value:	
			temp.next = self.head
			self.head = temp
		else:
			current = self.head			# traverse till current.next is less then new node's value
			while current.next != None and current.next.value < temp.value:
				current = current.next
			temp.next = current.next
			current.next = temp

	""" Print linked list"""
	def printList(self):
		current = self.head
		if self.head is not None:
			while current != None:
				print current.value,"-->",
				current = current.next
			print None
		else:
			"No linked list exists"
		
# program starts from here
if __name__ == "__main__":
	Llist = Linkedlist()
	print "Menu: "
	print "1 - insert new node into linked list in sorted manner "
	print "2 - print list"
	n = raw_input("Enter any number 1/2 : ")
	while True:
		if n == '1':
			value = input("Enter any value to append to node : ")
			Llist.insert_in_sorted_list(value)
		elif n == '2':
			Llist.printList()
		else:
			print "Invalid option choosen. Exiting...."
			break
		n = raw_input("Enter any number 1/2 : ")
				
