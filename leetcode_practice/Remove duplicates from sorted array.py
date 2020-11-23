class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen_Numbers = set()
        max_index= len(nums) -1
        counter= 0
        while counter <= max_index :
            if nums[counter] in seen_Numbers:
                seen_Numbers.remove(nums[counter])
                nums.remove(nums[counter])
               
                counter = counter -1
                max_index = len(nums) -1
            else:
                seen_Numbers.add(nums[counter])
                counter+=1
                