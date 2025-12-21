#define class
class Solution(object):

    #define method with input nums[]
    def findDisappearedNumbers(self, nums):

        result=[]                   #empty list to store missing values
        n=len(nums)                 #number of elements in nums[]

        for i in range(1,n+1):      #loop through 1 - n

            if i not in nums:          #for each i value, loop through nums[] to check existence
                result.append(i)        # add to result[] in not found

        return result