from typing import List


class Solution:
    """
        Ex: 
            students    = [1, 0, 0, 1, 1]
            sandwiches  = [0, 0, 1, 1, 0]
        
        The only time all students will eat is when we have the following: 
        #0s && #1s in the students list == #0s && #1s in the sandwiches list

        If either mismatch, then there will be students left to eat. The count in this case can differ based on
        the order of the sandwiches list, which is relevant. 

        The idea here is to use a HashMap to keep a count of the preferences of the students, 
        i.e. # of students with preference 0 and # of students with preference 1

        We want to count the number of students who are left to eat, and return it. We will initially set this
        to the length of the students list

        We pass through the sandwiches list, and: 
            - if we see a student with that preference, we can decrement the count for that sandwich preference
            and also the count of students that need to eat, because we have a match in the students list. 
            - if we don't see a student with that preference, then we can immediately return

        Once we visited all the sandwitches in the sandwitches list, we will be returning the number of 
        students left to eat


        Note --> The order of the students in the queue is not relevant as long as they can eat, 
        i.e. have a correspondence in the sandwiches stack. 
        However, the order in the sandwiches list does matter.
    """


    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        res = len(students)
        #cnt = Counter(students)
        cnt = {0: 0, 1: 0}
        # building our HashMap with students preferences
        for s in students:
            cnt[s] += 1
        
        # pass through the sandwiches list
        for s in sandwiches:

            # if we have an occurrece in the students list
            # we can decrement the number of students left to eat
            # we can also decrement the count of that preference occurrence
            
            if cnt[s] > 0:
                res -= 1        # decrement students left to eat
                cnt[s] -= 1     # decrement preference count

            else:               # if there are no occurrence in the students list, we have a mismatch
                return res      # we can immediately return 
        
        return res

        
        