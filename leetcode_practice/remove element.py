class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums: #while val exist in nums
            nums.remove(val) #