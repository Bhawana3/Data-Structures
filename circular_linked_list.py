class Node:
	# Constructor to create a new node
	def __init__(self):
		self.value = 0
		self.next = None
	
class CircularLinkedList:
	 # Constructor to create a new linked list
	def __init__(self):
		self.head = None
	
	""" Function to insert a node at the beginning of a
   		circular linked list"""	
	def insert_into_circular_list(self,value):
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

	def print_list(self):
		current = self.head
		if self.head is not None:
			while True :
				print current.value,"-->",
				current = current.next
				if current == self.head:
					break 
			print "end"
		else:
			print "No linked list exists"

if __name__ == '__main__':
	Llist = CircularLinkedList()
	print "Menu : "
	print "1  - append into circular linked list"
	print "2 - print circular linked list"
	n = raw_input("Choose number between 1/2 : ")
	while True:
		if n == '1':
			value = input("Enter any value which is to be appended into list : ")
			Llist.insert_into_circular_list(value)
		elif n == '2':
			Llist.print_list()
		else:
			print "Invalid option choosen. Exiting..."
			break
		n =raw_input("Choose number between 1/2 : ")
