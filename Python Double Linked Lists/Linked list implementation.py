


class node:
	def __init__(self , data = None):
		self.previous  = None
		self.data = data
		self.next = None





class LinkedList():
	def __init__(self):
		self.head = node()
		


	def append_node(self ,data):
		current_node = self.head
		while current_node.next != None:
			current_node = current_node.next

		new_node = node(data)
		new_node.previous = current_node
		current_node.next = new_node

	def all_nodes(self):
		current_node = self.head
		holder = []
		while current_node.next != None:
			current_node = current_node.next
			holder.append(current_node.data)


		return holder

	def index_points_to(self,index):
		current_node = self.head
		holder = 0
		data = None
		while current_node != None:
			
			if index == holder:
				data = current_node.previous.data
				break
			else:
				current_node = current_node.next
				holder +=1

		return data
ll = LinkedList()
ll.append_node(4)
ll.append_node(2)
ll.append_node(11)
print(ll.all_nodes())
print(ll.index_points_to(3))