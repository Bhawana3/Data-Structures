class Node():
	def __init__(self,value=0):
		self.value = value
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None
	
	def find_length_of_linked_list(self):
		current = self.head
		counter = 0
		if self.head is not None:
			while current.next != None:
				current = current.next
				counter += 1
			return counter + 1
		else:
			return 0


	def insert_node(self,position,value):
		temp = Node(value)
		current = self.head
		if self.head is not None:
			if position > 1:
				counter = 1
				while counter < position:			# as temp will be inserted at position-1 
					if counter == (position - 1) :		# node present at position will now move to position+1
						temp.next = current.next
						current.next = temp
					current = current.next
					counter += 1
			elif position == 1:					# first position of linked list
				temp.next = self.head
				self.head = temp
			else:
				return "position does not exists"
		else:	
			if position == 1:
				self.head = temp
				temp.next = None
			else:
				return "position does not exists"

	def print_list(self):
		print "printing linked list"
		current = self.head
		while current != None:
			print current.value , "-->",
			current = current.next
		print None
	
if __name__ == "__main__":
	List = LinkedList()
	n = raw_input("Enter number between 1/2/3:")
	while True:
		if n == '1':
			print List.find_length_of_linked_list()
		elif n == '2':
			pos = input("Enter any position to insert node:")
			val = input("Enter any value of node:")
			print List.insert_node(pos,val)
		elif n == '3':
			List.print_list()
		else:
			print "Invalid option choosen.Exiting..."
			break
		n = raw_input("Enter number between 1/2/3: ")
		
				
