class Node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self,value):
		self.root = Node(value)
	
	def InorderTreeTraversal(self,root):
		if root:
			self.InorderTreeTraversal(root.left)
			print root.value,
			self.InorderTreeTraversal(root.right)

	def PreOrderTreeTraversal(self,root):
		if root:
			print root.value,
			self.PreOrderTreeTraversal(root.left)
			self.PreOrderTreeTraversal(root.right)

	def PostOrderTreeTraversal(self,root):
		if root:
			self.PostOrderTreeTraversal(root.left)
			self.PostOrderTreeTraversal(root.right)
			print root.value,

	# search value in binary tree
	def search(self,root,given_value):
		if root:
			if root.value == given_value: 
				return True
			return self.search(root.left,given_value) or self.search(root.right,given_value)
		return False
 
tree = BinaryTree(1)
tree.root.left      = Node(2)
tree.root.right     = Node(3)
tree.root.left.left  = Node(4)
tree.root.left.right  = Node(5)
print "Preorder traversal of binary tree is"
tree.PreOrderTreeTraversal(tree.root)
 
print "\nInorder traversal of binary tree is"
tree.InorderTreeTraversal(tree.root)
 
print "\nPostorder traversal of binary tree is"
tree.PostOrderTreeTraversal(tree.root)

print "\nsearch given value"
print tree.search(tree.root,2)
