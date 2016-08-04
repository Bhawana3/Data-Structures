class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def Inordertraverse(self,root):
        if root:
            self.Inordertraverse(root.left)
            print root.value,
            self.Inordertraverse(root.right)

    def preorder(self,root):
        if root:
            print root.value,
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print root.value,
    
    def height_of_tree(self,root):
        if root is None:
            return 0
        lheight = self.height_of_tree(root.left)
        rheight = self.height_of_tree(root.right)

        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

    # print level order traversal of tree
    def printgivenlevel(self,root,level):
        if root is None:
            return
        elif level == 1:
            print root.value,
        elif level > 1:
            self.printgivenlevel(root.left,level-1)
            self.printgivenlevel(root.right,level-1)

    def printlevelorder(self,root):
        h = self.height_of_tree(root)
        for i in range(h+1):
            self.printgivenlevel(root,i)

    # find diameter of a tree(longest path between two nodes)
    def diameter(self,root):
        if root is None:
            return 0
        ldiameter = self.diameter(root.left)
        rdiameter = self.diameter(root.right)

        lheight = self.height_of_tree(root.left)
        rheight = self.height_of_tree(root.right)

        return max(lheight+rheight+1,ldiameter,rdiameter)

    # find the size of tree i.e how many nodes are there in tree
    def size_of_tree(self,root):
        if root is None:
            return 0
        size_of_left_tree = self.size_of_tree(root.left)
        size_of_right_tree = self.size_of_tree(root.right)
        return size_of_left_tree + size_of_right_tree + 1

    # count number of nodes at each level
    def count_nodes_at_level(self,root,level):
        if root is None:
            return 0
        elif level == 1:
            return 1
        elif level > 1:
            return self.count_nodes_at_level(root.left,level-1) + self.count_nodes_at_level(root.right,level-1)

    # calculate maximum width of binary tree
    def maximum_width(self,root):
        h = self.height_of_tree(root)
        max_width = 0
        for i in range(h+1):
            width = self.count_nodes_at_level(root,i)
            if max_width < width:
                max_width = width
        return max_width

    # check if two trees are identical
    def Identical_trees(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            return root1.value == root2.value and self.Identical_trees(root1.left,root2.left) and self.Identical_trees(root1.right,root2.right)
            return False

    # delete tree
    def deleteTree(self, root):
        if root is None:
            return
        self.deleteTree(root.left)
        self.deleteTree(root.right)
        print "Deleted node is : ", root.value 
        root.left = root.right = None
        self.root = None
            
        
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)

    tree2 = BinaryTree()
    tree2.root = Node(1)
    tree2.root.left = Node(2)
    tree2.root.right = Node(3)
    tree2.root.left.left = Node(4)
    tree2.root.left.right = Node(8)
    
    print "Inorder traversal: ",
    tree.Inordertraverse(tree.root)
    print "\npre-order traversal : ",
    tree.preorder(tree.root)
    print "\npost-order traversal:",
    tree.postorder(tree.root)
    print "\nheight of tree :", 
    print tree.height_of_tree(tree.root)
    print "level order traversal of tree :",
    tree.printlevelorder(tree.root)
    print "\ndiameter of the tree is : ",
    print tree.diameter(tree.root)
    print "size of tree is : ",
    print tree.size_of_tree(tree.root)
    print "maximum width of given binary tree is : ",
    print tree.maximum_width(tree.root)
    print "find if the trees are identical or not :",
    print tree.Identical_trees(tree.root,tree2.root)
    tree2.deleteTree(tree2.root)
    print "Tree Deleted"
