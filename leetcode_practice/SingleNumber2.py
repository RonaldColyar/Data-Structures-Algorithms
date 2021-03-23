
'''

Given an integer array nums where every element appears three times except for one, which appears exactly once.
 Find the single element and return it.

 

Runtime: 48 ms, faster than 96.89% of Python3 online submissions for Single Number II.
Memory Usage: 16 MB, less than 46.81% of Python3 online submissions for Single Number II.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_table = {}
        for i in nums:
            if i not in nums_table:
                nums_table[i] = 1
            else:
                nums_table[i] +=1
        for i in nums:
            if nums_table[i] < 3:
                return i 
                