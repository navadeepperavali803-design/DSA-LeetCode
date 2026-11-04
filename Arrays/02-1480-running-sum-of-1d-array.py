class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        ans=[]
        for num in nums:
            total = total + num
            ans.append(total)
        return ans
