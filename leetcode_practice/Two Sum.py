



"""



Runtime: 48 ms, faster than 76.35% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 96.48% of Python3 online submissions for Two Sum.

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {} # using a hashtable  for constant time lookup(assuming no collisons)
        if len(nums) == 2: # if there is only 2 elements. since the problem allows us to assume there is always one solution
            return [0,1]
        else:
            for i in range(0,len(nums)):
                valid_other = target - nums[i] #the other number we need for a solution. 

                if valid_other in table:
                    valid_other_index = table[valid_other]
                    index_pair = [i,valid_other_index]
                    return index_pair
                else:
                    table[nums[i]] = i
        