

"""

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Runtime: 172 ms, faster than 44.67% of Python3 online submissions for Majority Element.
Memory Usage: 15.6 MB, less than 49.19% of Python3 online submissions for Majority Element.


"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        holder = {}

        for i in nums:
            if i not in holder:
                holder[i] = 1
            else:
                holder[i] +=1
        for i in nums:
            if holder[i] > len(nums)/2:
                return i
        