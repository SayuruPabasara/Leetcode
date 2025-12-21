class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        counts=[0]*len(nums)
        for i in range(len(nums)):
            j=0
            for k in range(len(nums)):
                if k!=i and nums[k]<nums[i]:
                    j+=1
            counts[i]=j
        return counts        

        