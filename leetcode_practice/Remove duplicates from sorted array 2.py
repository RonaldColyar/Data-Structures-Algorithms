

"""
Runtime: 56 ms, faster than 41.59% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 14.6 MB, less than 23.44% of Python3 online submissions for Remove Duplicates from Sorted Array II.


medium question
"""






class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        table = {}
        max_index = len(nums) -1
        index = 0
        while index<= max_index:
            print(nums[index])
            if nums[index] in table and table[nums[index]] == 2: # if we see the number and it has been spotted twice 
                table[nums[index]] = 1 # setting the count to 1 since there is only 1 known to exist in the array
                nums.remove(nums[index]) # remove it from the array
                max_index = len(nums)-1 # updating the size of the max_index since we are deleting items from nums
                index  -=1 #decreasing the index since the overal size of the array is lower due to the last item getting removed
                print(nums)
               
            else:
                if nums[index] not in table:
                    table[nums[index]] = 1
                    
                else: # if it is in the table add one to it
                    
                    table[nums[index]] = 2
                    
                index +=1
          
        return len(nums)
        
        