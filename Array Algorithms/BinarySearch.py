



class BinarySearcher:
		def __init__(self, sorted_list):
		 	self.list = sorted_list


		def search_for(self , target):
			start_index = 0 #beginning of the search range
			end_index = len(self.list) -1 # end of the search range

			while start_index<= end_index: # while both indexes don't cross

				middle_point = start_index + (end_index - start_index) // 2 # middle point of the sorted array
				current_index_value = self.list[middle_point]

				if current_index_value == target: 
					return middle_point

				# since we know the list is sorted we can move the high index(end_index) down to the
				#index one less than the middle point and eliminate the other elements that come after
				#the middle point which will be better than a linear solution O(n). Log n 
				#every loop will shorten the search parameters.

				elif target < current_index_value : 
					end_index = middle_point -1

				else:
					start_index = middle_point+1

			return None

				


binary_obj= BinarySearcher([2,10,20,30,40,50,110,200,300,400])
print(binary_obj.search_for(40))