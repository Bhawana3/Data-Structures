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

	
	# print out all the nodes from root to leaf
	def printTree(self,root,pathlen,pathlist):
		if root is None:
			return
		
		pathlist.insert(pathlen,root.value)
		pathlen += 1
		if root.left is None and root.right is None:
			print pathlist[0:pathlen]
		else:
			if root.left is not None:
				self.printTree(root.left,pathlen,pathlist)
			if root.right is not None:
				self.printTree(root.right,pathlen,pathlist)

	# convert a tree into its mirror 
	def mirrorTree(self,root):
		temp = Node(0)
		if root is None:
			return 
		self.mirrorTree(root.left)
		self.mirrorTree(root.right)
		temp = root.left
		root.left = root.right
		root.right = temp

# build tree from given preorder and inorder sequence
def buildBT(preorder,pstart,pend,inorder,instart,inend):
	if pstart > pend or instart > inend:
		return None
	value = preorder[pstart]
	temp = Node(value)
	i = instart
	while i < inend:
		if inorder[i] == value:
			break
		i += 1
	# recur on left child
	temp.left = buildBT(preorder,pstart+1,i+pstart-instart,inorder,instart,i-1)
	# recur on right child
	temp.right = buildBT(preorder,i+pstart-instart+1,pend,inorder,i+1,inend)	
	return temp

def buildTree(preorder,inorder):
	if len(preorder) == 0 or len(preorder) != len(inorder):
		return None
	return buildBT(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)

# build tree using inorder anf post order traversal
def buildTreePost(postorder,pstart,pend,inorder,instart,inend):
	if pstart > pend or instart > inend:
		return None
	data = postorder[pend]
	temp = Node(data)
	i = instart
	while i < inend:
		if inorder[i] == data:
			break
		i += 1
	temp.left = buildTreePost(postorder,pstart,pstart+i-instart-1,inorder,instart,i-1)
	temp.right = buildTreePost(postorder,pstart+i-instart,pend-1,inorder,i+1,inend)
	return temp
	
def buildBTree(postorder,inorder):
	if len(postorder) == 0 or len(postorder) != len(inorder):
		return None
	return buildTreePost(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1)

def printInorder(node):
    if node is None:
        return
     
    # first recur on left child
    printInorder(node.left)
     
    #then print the data of node
    print node.value,
 
    # now recur on right child
    printInorder(node.right)

# Driver code
if __name__ == "__main__":
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
	print "\nprint nodes from root to leaf:",
	tree.printTree(tree.root,pathlen=0,pathlist=[])
	print "\nconverting tree into its mirror tree"
	tree.mirrorTree(tree.root)
	print "\nInorder traversal of mirror tree: ",
	tree.InorderTreeTraversal(tree.root)
	print "\nbuild tree from given inorder and preorder sequence"
	tree2 = buildTree(['A','B','C','D','E','F','G'],['C','B','D','A','F','E','G'])
	print "inorder sequence of build tree:",
	printInorder(tree2)
	print "\nbuild tree from given inorder and postorder sequence"
	tree3 = buildBTree(['C','D','B','A','E'],['C','B','D','A','E'])
	print "inorder sequence of build tree from inorder and post order sequence:",
	printInorder(tree3)
