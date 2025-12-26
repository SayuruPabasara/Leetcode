class Solution(object):
    def countStudents(self, students, sandwiches):
        count0=students.count(0)
        count1=students.count(1)
        for s in sandwiches:
            if s==0:
                if count0==0:
                    break
                else:
                    count0-=1
            else:
                if count1==0:
                    break
                else:
                    count1-=1
        return count0+count1       
