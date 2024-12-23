class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res
        """
        Hash set cozumu 
        hashset = set()
        for num in nums:
            if num in hashset:
                hashset.remove(num)
                continue
            hashset.add(num)
        for x in hashset:
            return x
            
        First Solution
        if len(nums) == 1:#Edge Case
            return nums[0]
        for i in range(0,len(nums)):
            temp = nums[i]
            nums.pop(i)
            if temp not in nums:
                nums.insert(i,temp)
                return temp
            nums.insert(i, temp)
        """
sol = Solution()
print(sol.singleNumber([-1,-1,-2]))