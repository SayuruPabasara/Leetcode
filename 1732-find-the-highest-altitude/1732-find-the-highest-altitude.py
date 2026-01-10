class Solution(object):
    def largestAltitude(self, gain):
        highest=0
        sums=0
        for g in gain:
            sums+=g
            if sums>=highest:
                highest=sums
        return highest


        