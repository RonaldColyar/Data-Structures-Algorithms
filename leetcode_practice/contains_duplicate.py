


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = set()
        for i in nums:
            if i in seen_numbers:
                return True
            else:
                seen_numbers.add(i)
        return False