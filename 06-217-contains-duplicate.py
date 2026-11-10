class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        counts={}
        for num in nums:
            if num in counts:
                counts[num]+=1
                if counts[num]>1:
                    return(True)
            else:
                counts[num]=1
        return(False)
