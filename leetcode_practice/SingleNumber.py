class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_table = {}
        for i in nums:
            if i not in nums_table:
                nums_table[i] = 1
            else:
                nums_table[i] +=1
        for i in nums:
            if nums_table[i] == 1:
                return i 
                
            
        