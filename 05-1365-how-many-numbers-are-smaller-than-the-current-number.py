class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans_nums=[]
        for num in nums:
            count=0
            for value in nums:
                if value < num:
                    count += 1
            ans_nums.append(count)
        return ans_nums
