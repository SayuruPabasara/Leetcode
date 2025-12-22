class Solution(object):
    def buildArray(self, target, n):
        ops=[]
        targetSet=set(target)
        for i in range(1,n+1):
            if i in targetSet:
                ops.append("Push")
            else:
                ops.append("Push")
                ops.append("Pop")
            if  i==target[len(target)-1]:
                break   
        return ops

        