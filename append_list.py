class Node():
	def __init__(self,value=0):
		self.value = value
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None		# head refers to empty linked list 
	
	def append(self,value):			# input value of node
		temp = Node(value)		# new node to be appended with node value equals to value 
		current = self.head
		if self.head is not None:
			while current.next != None:
				current = current.next
			current.next = temp
		else:
			self.head = temp 
	
	def traverse(self):			# finds the length of list	
		counter = 0 
		current = self.head
		if self.head is not None:
			while current != None:
				current = current.next
				counter += 1
			print counter
			return counter
		return counter
	
	def get_position(self,position):	# given position finds the value of node at that position
		current = self.head
		counter = 0 
		if position >= 0 :
			while self.head:
				if counter == position:
					print current.value
					return current.value
				else:
					current = current.next
				counter += 1
		else:
			print None
			return None

	def print_linked_list(self):
		current = self.head
		if self.head is not None:
			while current != None:
				print current.value,"-->",
				current = current.next
			print "NULL"
		else:
			"No linked list exists"				


if __name__ == "__main__":
	List = LinkedList()
	print "Menu:"
	print "1 - Append and element to the linked list"
	print "2 - Find the length of linked list"
	print "3 - Find the node at position entered by user"
	print "4 - Print linked list"
	
	n = raw_input("Choose an option(1/2/3/4) :")
	while True:
		if n == '1':
			val = input("Enter any value to append to the list:")
			List.append(val)
		elif n == '2':
			List.traverse()
		elif n == '3':
			pos = input("Enter any position to find the value of node:")
			List.get_position(pos)
		elif n == '4':
			List.print_linked_list()
		else:
			print "Invalid option choosed.Exiting ...."
			break
		n = raw_input("Choose an option(1/2/3/4): ")
		
		 
