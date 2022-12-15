from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools
student_roster_iter = iter(student_roster)
for i in range(10):
    #printing the next value in student_roster_iter
    print(next(student_roster_iter))

classroom = ClassroomOrganizer()
#print(classroom1.student_combination())
#task 5
Student_Math_Science = itertools.chain(classroom.get_students_with_subject("Math"),classroom.get_students_with_subject("Science"))
print(Student_Math_Science)
print(list(itertools.combinations(Student_Math_Science, 4)))