class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

class BalancedBinarySearchTree:
	def __init__(self):
		self.root = None
		raise NotImplementedError

	def insert(self, number):
		if not self.root:
			self.root = Node(number)
			return self.root
		currentNode = self.root
		while True:
			if number>currentNode.data:
				if currentNode.right:
					currentNode = currentNode.right
				else:
					currentNode.right = Node(number)
					return self.root
			else:
				if currentNode.left:
					currentNode = currentNode.left
				else:
					currentNode.left = Node(number)
					return self.root
		return self.root
		raise NotImplementedError

	def remove(self, number):
		#remove number from BST
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
