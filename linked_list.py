class Node():
	def __init__(self,value=0):
		self.value = value
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None		# head refers to empty linked list 
	
	""" append(insert node in the last) new node in the linked list"""
	def append(self,value):			# input value of node
		temp = Node(value)		# new node to be appended with node value equals to value 
		current = self.head
		if self.head is not None:
			while current.next != None:
				current = current.next
			current.next = temp
		else:
			self.head = temp 
	
	""" Find the length of the linked list 
			or
	 traverse through the linked list"""
	def traverse(self):				
		counter = 0 
		current = self.head
		if self.head is not None:	#finds if list is not empty
			while current != None:
				current = current.next
				counter += 1
			return counter
		return counter
	
	""" Find the value of node at 
		given position"""
	def find_node_at_given_position(self,position):	
		current = self.head
		counter = 0 
		if self.head is not None:
			if position >= 1 :
				while current != None:
					if counter == (position - 1):	# as counter starts from 0
						return current.value
					else:
						current = current.next
					counter += 1
			else:
				return None
		else:
			return "No linked list exists" 
	
	""" prints out linked list"""
	def print_linked_list(self):
		current = self.head
		if self.head is not None:
			while current != None:
				print current.value,"-->",		# prints out in single row
				current = current.next
		else:
			"No linked list exists"				
	
	""" Delete last node 
		from the linked list"""
	def delete_last_node(self):
		current = self.head
		if self.head is not None:
			next_element_of_current = current.next 
			if current.next == None:
				self.head = None
			else:
				while (next_element_of_current.next != None):
					current = current.next
					next_element_of_current = current.next
				current.next = None
		else:
			return "No linked list exists"	
	
	"""push a new node on the front
   		 of the list."""
	def push_new_node_in_front(self,value):			# push new node in front of the linked list
		temp = Node(value)			# creates new node having reference temp
		if self.head is not None:			# if linked list is not empty
			temp.next = self.head			# temp points towards head
			self.head = temp			# make head and temp equal
		else:
			self.head = temp			# when linked list is empty
			temp.next = None		

if __name__ == "__main__":
	List = LinkedList()
	print "Menu:"
	print "1 - Append an element to the linked list"
	print "2 - Find the length of linked list"
	print "3 - Find the node at position entered by user"
	print "4 - Print linked list"
	print "5 - Delete last element from linked list"
	print "6 - Push new node in front of the linked list"
	n = raw_input("Choose an option(1/2/3/4/5/6) :")
	while True:
		if n == '1':
			val = input("Enter any value to append to the list:")
			List.append(val)
		elif n == '2':
			print List.traverse()
		elif n == '3':
			pos = input("Enter any position to find the value of node:")
			print List.find_node_at_given_position(pos)
		elif n == '4':
			print List.print_linked_list()
		elif n == '5':
			print List.delete_last_node() 
		elif n =='6':
			val = input("Enter any value to push into the linked list:")
			List.push_new_node_in_front(val)
		else:
			print "Invalid option choosed.Exiting ...."
			break
		n = raw_input("Choose an option(1/2/3/4/5/6): ")
		
		 
