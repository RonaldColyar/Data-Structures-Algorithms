
'''

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once. You can return the answer in any order.


Runtime: 56 ms, faster than 85.96% of Python3 online submissions for Single Number III.
Memory Usage: 16 MB, less than 43.62% of Python3 online submissions for Single Number III.
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        nums_table = {}
        for i in nums:
            if i not in nums_table:
                nums_table[i] = 1
            else:
                nums_table[i] += 1
                
        single_apperances = []
        for i in nums:
            if nums_table[i] == 1:
                single_apperances.append(i)
        return single_apperances
        