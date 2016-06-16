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
		if current != None:
			while current.next != None:
				current = current.next
				counter += 1
			return counter + 1

	""" Method-1 : to get the middle node of linked list"""	
	def find_middle_node(self):
		n = self.find_length_of_linked_list()	# for calling find_length method	
		print "length_of_list: ",n
		counter = 1
		current = self.head
		if current is not None:
			if n > 1:
				if n % 2 == 0:
					while counter < ((n/2) + 1):
						current = current.next
						counter += 1
					if counter == (n/2)+1:
						return current.value
				else:
					while counter < ((n+1)/2):
						current = current.next
						counter += 1	
					if counter == (n+1)/2 :
						return current.value
			else:
				return current.value 
		else:
			return "No linked list exists"

	"""Method-2 : To get the middle node of linked list """	
	def find_middle_node_second_method(self):
		slow = self.head
		fast = self.head
		if self.head is not None:
			while fast != None and fast.next != None:
				slow = slow.next			# moves with v speed		
				fast = fast.next.next			# moves with 2v speed therefore slow always be the half of fast
			return slow.value
		else:
			return "No linked list exists"

	def append_list(self,value):
		temp = Node(value)
		current = self.head
		if current is not None:
			while current.next != None:
				current = current.next
			current.next = temp
		else:
			self.head = temp
	
	def print_list(self):
		current = self.head
		if self.head is not None:
			while current != None:
				print current.value , "-->",
				current = current.next
			print None
		else:
			print "No linked list exists"
							

if __name__ == "__main__":
	List = LinkedList()
	print "Menu :"
	print "1 - Find length of linked list"
	print "2 - Method1-Find middle node of linked list"
	print "3 - Method2-Find middle node of linked list"
	print "4 - Append node into list"
	print "5 - Print list"

	n = raw_input("Enter number 1/2/3/4/5 :")
	while True:
		if n == '1':
			print List.find_length_of_linked_list()
		elif n == '2':
			print List.find_middle_node()
		elif n == '3':
			print List.find_middle_node_second_method()
		elif n =='4':
			val = input("Enter value to append : ")
			print List.append_list(val)
		elif n == '5':
			print List.print_list()	
	
		else:
			print "Wrong option choosen. Exiting..."
			break
		n = raw_input("Enter number 1/2/3/4/5 :")
