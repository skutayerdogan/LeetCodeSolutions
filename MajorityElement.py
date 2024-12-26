class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Boyer Moore
        result = 0
        count = 0
        for num in nums:
            if count == 0:
                result = num
            count += 1 if num == result else -1
        return result

        """
        First Solution
        if len(nums) == 1: #Edge Case
            return nums[0]
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] = dic[num] + 1
                if dic[num] > len(nums)/2:
                    return num
                continue
            dic[num] = 1
        """
        """
        Second Solution
        numbers = {}
        result = 0
        maxNum = 0
        for num in nums:
            numbers[num] = numbers.get(num,0) + 1
            if numbers[num] > maxNum:
                result = num
            maxNum = max(maxNum,numbers[num])
        return result
        """

sol = Solution()
sol.majorityElement([1])
sol.majorityElement([2,2,1,1,1,2,2])