class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
        """"
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
        """