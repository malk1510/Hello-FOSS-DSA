class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
		self.height = 0

class BalancedBinarySearchTree:
	def __init__(self):
		self.root = None
		raise NotImplementedError
	
	def right_rotate(self, root):
		node = root.left
		root.left = node.right
		node.right = root
		return node
	
	def left_rotate(self, root):
		node = root.right
		root.right = node.left
		node.left = root
		return node
	def insert(self, number, root = self.root):
		if root.data<number:
			if root.right:
				root.right = self.insert(number,root.right)
			else:
				root.right = Node(number)
		else:
			if root.left:
				root.left = self.insert(number,root.left)
			else:
				root.left = Node(number)
		root.height+=1
		h_l = root.left.height if root.left else -1
		h_r = root.right.height if root.right else -1
		if abs(h_r-h_l)<2:
			return root
		if h_r>h_l:
			node = root.right
			if (not node.right or node.right.height<node.left.height):
				root.right = self.right_rotate(node)
			root = self.left_rotate(root)
		else:
			node = root.left
			if (not node.left or node.left.height<node.right.height):
				root.left = self.left_rotate(node)
			root = self.right_rotate(root)
		return root

	def remove(self, number):
		
		raise NotImplementedError

	def greater_than_equal(self, number):
		#find number in BST greater than equal to number. Return -1 if does not exist.
		raise NotImplementedError


def main():
	f = open("test.in", "r")
	## handle input here from f 
	bst = BalancedBinarySearchTree()

	# handle operations and print to terminal

	f.close()

if __name__=='__main__':
	main()
