


class node:
	def __init__(self,data = None):
		#pointer to the next node
		self.next = None
		self.data = data




class linked_list:
	def __init__(self):
		self.head = node()


	def append_node(self,data):#O(n)
		new_node = node(data)

		current_node = self.head #starting with our reference point
		while current_node.next != None : # keep traversing through the list until we find the end 
			current_node = current_node.next
		current_node.next = new_node #update the end with the new node

	def all_elements_data(self): #O(n)
		current_node = self.head
		holder = []

		while current_node.next != None:
			current_node = current_node.next
			holder.append(current_node.data)
			
		return holder

	def length(self): #O(n)
		current_node = self.head
		counter = 0
		while current_node.next != None:
			current_node = current_node.next
			counter+=1
		return counter
	def remove_target(self,target): #O(n)
		current_node = self.head

		while current_node.next != None:
			if current_node.next.data == target: #if the data matches what we are trying to remove
				current_node.next = current_node.next.next #update current node pointer to the removed nodes pointer
				break
			else:
				current_node = current_node.next

	def check_index(self,index):
		if index < 1:
			return False
		else:
			return True
	def indexof(self , target):
		current_node = self.head
		index = 0
		while current_node.next != None:
			if current_node.data == target:
				break
			else:
				index+=1
				current_node = current_node.next


		if index < 1:
			return -1
		else:
			return index

ll = linked_list()
ll.append_node(3)
ll.append_node(2)
ll.append_node(2)
ll.append_node(2)
ll.append_node(7)
ll.append_node(0)
print(ll.indexof(7))