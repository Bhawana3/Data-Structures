class Node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None
	
	def insert(self,root,new_val):
		if root is None:
			root = Node(new_val)
		else:
			if root.value < new_val:
				if root.right is None:
					root.right = Node(new_val)
				else:
					self.insert(root.right,new_val)
			else:
				if root.left is None:
					root.left = Node(new_val)
				else:
					self.insert(root.left,new_val)


	def binarySearch(self,root,value):
		if root:
			if root.value == value:
				return True
			elif root.value > value:
				return self.binarySearch(root.left,value)
			else:
				return self.binarySearch(root.right,value)
		return False

if __name__ == "__main__":
	tree = BinarySearchTree()
	tree.root = Node(11)
	tree.root.left = Node(8)
	tree.root.left.left = Node(5)
	tree.root.left.right = Node(10)
	tree.root.right = Node(12)
	tree.root.right.left = Node(9)
	tree.root.right.right = Node(15)
	print "Searching value in binary search tree : ",
	print tree.binarySearch(tree.root,19)
	print "Inserting node into tree",
	tree.insert(tree.root,7)
	print "\ninserted value exists in tree: ",
	print tree.binarySearch(tree.root,7)
