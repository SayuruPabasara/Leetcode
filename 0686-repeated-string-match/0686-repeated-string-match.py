class Solution(object):
    def repeatedStringMatch(self, a, b):
        if a in b:
            index=b.find(a)
            new_b=b[index:]+b[:index]
            counts=new_b.count(a)
            if index!=0:
                counts+=1
            return counts
        else:
            return -1