class Solution(object):
    def countStudents(self, students, sandwiches):
        st_set=set(students)
        while sandwiches and sandwiches[0] in st_set: 
            if sandwiches[0]==students[0]:
                sandwiches.pop(0)
                students.pop(0)
                st_set=set(students)
            else:
                students.append(students.pop(0))
        return len(students)





            
        