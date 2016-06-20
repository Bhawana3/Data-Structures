class Node():
    def __init__(self,value=0):
            self.value = value
            self.next = None

class LinkedList():
        def __init__(self):
                self.head = None
        def append(self,value):
            temp = Node(value)
            current = self.head
            if self.head is not None:
                while current.next is not None:
                    current = current.next
                current.next = temp
                temp.next = None
            else:
                self.head = temp
                temp.next = None

	def get_middle_element(self):
	    mid = None
	    if self.head == None:
		return mid
	    else:
		length = 0
		current = self.head
		while current != None:
		    length += 1
		    current=current.next
		# Now find the middle element
		# We're assuming that middle element is
		# (length/2)th element
		current = self.head
		ctr = 0
		while ctr < length/2:
		    current = current.next
		    ctr+=1
	        mid = current
		return mid
		

	""" Given only a single node to be deleted
	in a linked list, how to delete that node"""
        def delete_node_with_given_pointer(self,node):
	    if node == None:
		print "Linked list is None"
	    elif node.next == None:
		print "This is the last node of linked list, and hence can't be deleted"
	    else:
            	temp = node.next
            	node.value = temp.value
            	node.next = temp.next
	
	""" Delete Linked list"""
	def delete_linked_list(self):
		self.head = None		

        def print_linked_list(self):
            current = self.head
            if current is not None:
                while current is not None:
                    print current.value,'-->',
                    current = current.next
                print None
            else:
                print 'No linked list exists'

	""" Counts the no. of occurances of a node """
	def find_count_of_given_integer(self,integer):
		current = self.head
		count  = 0
		if current is not None:
			while current != None:
				if current.value == integer:
					count += 1
				current = current.next
			return count
		else:
			return 0
	
	""" pairwise swap elements of linked list """
	def swap(self):
		current = self.head
		while current != None and current.next != None:
			b = current.next.value 
			a = current.value
			current.value = b
			current.next.value = a
			current = current.next.next
		
	""" Move last from the front of given linked list"""	
	def move_last_to_front(self):
		current = self.head
		if current is not None and current.next is not None:		# linked list must have 1 node
			while current.next.next != None:
				current = current.next
			tail = current						# call second last node as tail
			temp = tail.next					# call last node as temp
			temp.next = self.head					
			tail.next = None					# make second last node into	 last node
			self.head = temp					# make head equal to temp
		else:
			"No linked list exists"	
	
if __name__ == '__main__':
    List = LinkedList()
    print 'menu:'
    print '1 - Append linked list'
    print '2 - delete node with given pointer'
    print '3 - print linked list'
    print '4 - find count of given integer'
    print '5 - swap values'
    print '6 - move last to front'
    print '7 - delete linked list'
    n = raw_input('Choose any number 1/2/3/4/5/6/7 :')
    while True:
        if n == '1':
            val = input('choose value to append into list:')
            List.append(val)
        elif n =='2':
	    middle_element = List.get_middle_element()
	    if middle_element is not None:
	    	print 'Trying to delete the middle element:',middle_element.value
            	List.delete_node_with_given_pointer(node=middle_element)
	    else:
		print 'Not doing anything as middle element is none'
        elif n =='3':
            List.print_linked_list()
	elif n == '4':
	    integer = input("Enter integer to know its counts:")	
	    print List.find_count_of_given_integer(integer)
	elif n == '5':
	   List.swap()
	elif n == '6':
	   List.move_last_to_front()
	elif n == '7':
	   List.delete_linked_list()
	else:
            print 'Invalid option choosen,quiting....'
            break
        n = raw_input('Choose any number 1/2/3/4/5/6/7 :')            
    
