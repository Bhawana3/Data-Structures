class Node:
	def __init__(self,value = 0):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	
	def append(self,value):
		temp = Node(value)
		current = self.head
		if current is not None:
			while current.next is not None:
				current = current.next
			current.next = temp
		else:
			self.head = temp
	def print_linked_list(self):
		current = self.head
		if current is not None:
			while current is not None:
				print current.value ,"-->",
				current = current.next
			print None
		else:
			return "list does not exists"
	
	"""Find length of linked list""" 
	def find_length(self):
		count= 0
		current = self.head
		if current is not None:
			while current is not None:
				current = current.next
				count += 1
			return count
		else:
			return 0	

	""" make intersecting linked lists"""
	def make_intersecting_linked_list(self,list3):
		current = self.head
		if current is not None:
			while current.next is not None:
				current = current.next
			current.next = list3.head
		else:	
			current = list3.head

""" Method-1 : Find intersection point of 2 linked lists"""
""" Time complexity - O(n*n)"""
def find_intersection(list1,list2):
	first = list1.head
	second = list2.head
	while first is not None: 
		while second is not None:
			if first != second:
				first = first.next
				second = second.next
			else:
				print "Lists intersect, value = " 
				return first.value
	return "Lists do not intersect."

""" Method -2 : Find intersection point of 2 linked lists"""
""" Time complexity - O(n+n)"""
def find_intersection_point(list1,list2):
	first = list1.head
	second = list2.head
	node_address = {}
	while first is not None:
		node_address[first]= first.value
		first = first.next
	while second is not None:
		address_second = second
		if address_second in node_address:
			print "Lists intersect, value = "
			return node_address[second]
		else:
			second = second.next
	return "Lists do not intersect"

""" Method-3 : Find intersection point using length of LL"""
""" Time complexity - O(n+n)"""
def find_intersection_using_length(list1,list2):
	first = list1.head
	second = list2.head
	length_of_list1 = list1.find_length()			
	length_of_list2 = list2.find_length()
	diff = length_of_list1 - length_of_list2
	count = 0
	if diff > 0:		
		while count < abs(diff) and first != None:	# move pointer till length of both lists becomes equal
			first = first.next
			count += 1
		print first.value
	else:
		while count < abs(diff) and second != None:
			second = second.next
			count += 1
		print second.value
		
	while first != None and second != None:			# move both pointers together till both pointer becomes equal
		if first != second:
			first = first.next
			second = second.next
		else:
			print "lists intersect, value ="
			return first.value
	return "Lists do not intersect"

if __name__ == "__main__":
	list1 = LinkedList()
	list2 = LinkedList()
	list3 = LinkedList()
	
	print "Menu : "
	print "1 - append node in list1"
	print "2 - append node in list2"
	print "3 - append node in list3"
	print "4 - print list1"
	print "5 - print list2" 			
	print "6 - print list3"
	print "7 - make list1 intersecting to list3"
	print "8 - make list2 intersecting to list3"
	print "9 - Find intersection point of 2 lists, list1 and list2 by method1" 
	print "10 - Find interesection point of 2 LL by method2"
	print "11 - Find interesection point of 2 LL by method3"

	n = raw_input("Choose any number 1/2/3/4/5/6/7/8/9/10/11 : ")
	while True:
		if n == '1':
			val = input("Enter value of node to be appended in list1 : ")
			list1.append(val)
		elif n == '2':
			val = input("Enter value of node to be appended in list2 : ")
			list2.append(val)
		elif n == '3':
			val = input("Enter value of node to be appended in list3 : ")
			list3.append(val)
		elif n == '4' :
			list1.print_linked_list()
		elif n == '5' :
			list2.print_linked_list()
		elif n == '6' :
			list3.print_linked_list()
		elif n == '7':
			list1.make_intersecting_linked_list(list3)
		elif n == '8':
			list2.make_intersecting_linked_list(list3)
		elif n == '9' :
			print find_intersection(list1,list2)
		elif n == '10':
			print find_intersection_point(list1,list2)
		elif n == '11':
			print find_intersection_using_length(list1,list2)
		else:
			print "Invalid option choosed.Exiting..."
			break
		n = raw_input("Choose any number 1/2/3/4/5/6/7/8/9/10/11 : ")
